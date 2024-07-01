from io import BytesIO

from flask import render_template, url_for, redirect

from models import db, ConciergeMiis, MiiMsgInfo, MiiData
from room import app
from theunderground.forms import ConciergeForm
from theunderground.operations import manage_delete_item
from theunderground.admin import oidc
from theunderground.encodemii import encode_mii_category
from room import s3
from url1.event_today import event_today
from url1.mii import obtain_mii, mii_met
from werkzeug import exceptions
from asset_data import NormalCategoryAsset

import config
import requests


@app.route("/theunderground/concierge")
@oidc.require_login
def list_concierge():
    concierge_miis = (
        db.session.query(ConciergeMiis, MiiData)
        .filter(ConciergeMiis.mii_id == MiiData.mii_id)
        .all()
    )

    return render_template(
        "concierge_list.html",
        miis=concierge_miis,
        type_length=len(concierge_miis),
        type_max_count=20,
    )


@app.route("/theunderground/concierge/<mii_id>/add", methods=["GET", "POST"])
@oidc.require_login
def add_concierge(mii_id):
    form = ConciergeForm()
    if form.validate_on_submit():
        concierge_data = ConciergeMiis(
            mii_id=mii_id,
            clothes=1,  # TODO: Allow disabling of custom clothes
            action=form.action.data,
            prof=form.prof.data,
            movie_id=form.movieid.data,
            voice=False,  # The web console does not currently support this
        )

        for i in range(1, 8):
            msg = MiiMsgInfo(
                mii_id=mii_id, type=i, msg=form[f"message{i}"].data, face=1
            )
            db.session.add(msg)

        # Create the category image.
        mii_data = MiiData.query.filter_by(mii_id=mii_id).first()
        if not mii_data:
            return exceptions.NotFound()

        # Request the PNG from Nintendo
        mii_img = requests.get(
            f"https://miicontestp.wii.rc24.xyz/cgi-bin/render.cgi?data={mii_data.data.hex()}"
        )

        img = encode_mii_category(mii_img.content)
        # We assign concierge categories IDs 20000 - 29999.
        NormalCategoryAsset(20000 + int(mii_id)).encode(img)

        db.session.add(concierge_data)
        db.session.commit()

        update_mii_on_s3(mii_id)
        return redirect(url_for("list_concierge"))

    return render_template("concierge_action.html", form=form, action="Add")


@app.route("/theunderground/concierge/<mii_id>/edit", methods=["GET", "POST"])
@oidc.require_login
def edit_concierge(mii_id):
    form = ConciergeForm()
    form.submit.label.text = "Edit"

    # Get current data
    retrieved_data = (
        db.session.query(ConciergeMiis, MiiMsgInfo)
        .filter(ConciergeMiis.mii_id == mii_id)
        .filter(ConciergeMiis.mii_id == MiiMsgInfo.mii_id)
        .order_by(MiiMsgInfo.type)
        .all()
    )

    if not retrieved_data:
        return exceptions.NotFound()

    # The above query returns a list with the first index being the Concierge Mii, and the rest being the messages.
    mii_msg_infos = retrieved_data

    if form.validate_on_submit():
        mii_msg_infos[0][0].action = form.action.data
        mii_msg_infos[0][0].prof = form.prof.data
        mii_msg_infos[0][0].movie_id = form.movieid.data

        for _, info in mii_msg_infos:
            info.msg = form[f"message{info.type}"].data

        db.session.commit()

        update_mii_on_s3(mii_id)
        return redirect(url_for("list_concierge"))
    else:
        # Populate the data
        form.action.data = mii_msg_infos[0][0].action
        form.prof.data = mii_msg_infos[0][0].prof
        form.movieid.data = mii_msg_infos[0][0].movie_id
        for _, info in mii_msg_infos:
            form[f"message{info.type}"].data = info.msg

    return render_template("concierge_action.html", form=form, action="Edit")


@app.route("/theunderground/concierge/<mii_id>/remove", methods=["GET", "POST"])
@oidc.require_login
def remove_concierge(mii_id):
    def drop_concierge():
        db.session.delete(ConciergeMiis.query.filter_by(mii_id=mii_id).first())
        db.session.delete(MiiMsgInfo.query.filter_by(mii_id=mii_id).first())
        db.session.commit()
        return redirect(url_for("list_concierge"))

    return manage_delete_item(mii_id, "Concierge Mii", drop_concierge)


def update_mii_on_s3(mii_id):
    if s3:
        # Update the today.xml
        event_xml = event_today()
        s3.upload_fileobj(BytesIO(event_xml), config.r2_bucket_name, "event/today.xml")

        # Metadata
        met = mii_met(mii_id)
        s3.upload_fileobj(BytesIO(met), config.r2_bucket_name, f"mii/{mii_id}.met")

        # Actual Mii
        mii = obtain_mii(mii_id)
        s3.upload_fileobj(BytesIO(mii), config.r2_bucket_name, f"mii/{mii_id}.mii")

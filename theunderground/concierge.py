# TODO: This is so flawed must fix later

from io import BytesIO

from flask import render_template, url_for, redirect

from models import db, ConciergeMiis, MiiMsgInfo, MiiData
from room import app
from theunderground.forms import ConciergeForm
from theunderground.operations import manage_delete_item
from theunderground.admin import oidc
from room import s3
from url1.event_today import event_today
from url1.mii import obtain_mii, mii_met
from werkzeug import exceptions

import config


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
            action=1,  # TODO: Allow changing of whatever the heck "action" is
            prof=form.prof.data,  # TODO: Add this.
            movie_id=form.movieid.data,
            voice=False,  # The web console does not currently support this
        )
        # I would **assume** that Mii data is already in the console.
        # Which saves us space in the UI
        # The below will be very messy, enjoy!
        msg1 = MiiMsgInfo(mii_id=mii_id, type=1, seq=1, msg=form.message1.data, face=1)
        msg2 = MiiMsgInfo(mii_id=mii_id, type=2, seq=1, msg=form.message2.data, face=1)
        msg3 = MiiMsgInfo(mii_id=mii_id, type=3, seq=1, msg=form.message3.data, face=1)
        msg4 = MiiMsgInfo(mii_id=mii_id, type=4, seq=1, msg=form.message4.data, face=1)
        msg5 = MiiMsgInfo(mii_id=mii_id, type=5, seq=1, msg=form.message5.data, face=1)
        msg6 = MiiMsgInfo(mii_id=mii_id, type=6, seq=1, msg=form.message6.data, face=1)
        msg7 = MiiMsgInfo(mii_id=mii_id, type=7, seq=1, msg=form.message7.data, face=1)
        # Now to add all of them
        db.session.add(msg1)
        db.session.add(msg2)
        db.session.add(msg3)
        db.session.add(msg4)
        db.session.add(msg5)
        db.session.add(msg6)
        db.session.add(msg7)
        db.session.add(concierge_data)
        db.session.commit()

        update_mii_on_s3(mii_id)
        return redirect(url_for("list_concierge"))

    return render_template("concierge_action.html", form=form)


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
        concierge_data = ConciergeMiis(
            mii_id=mii_id,
            clothes=1,  # TODO: Allow disabling of custom clothes
            action=1,  # TODO: Allow changing of whatever the heck "action" is
            prof=form.prof.data,  # TODO: Add this.
            movie_id=form.movieid.data,
            voice=False,  # The web console does not currently support this
        )
        # I would **assume** that Mii data is already in the console.
        # Which saves us space in the UI
        # The below will be very messy, enjoy!
        msg1 = MiiMsgInfo(mii_id=mii_id, type=1, seq=1, msg=form.message1.data, face=1)
        msg2 = MiiMsgInfo(mii_id=mii_id, type=2, seq=1, msg=form.message2.data, face=1)
        msg3 = MiiMsgInfo(mii_id=mii_id, type=3, seq=1, msg=form.message3.data, face=1)
        msg4 = MiiMsgInfo(mii_id=mii_id, type=4, seq=1, msg=form.message4.data, face=1)
        msg5 = MiiMsgInfo(mii_id=mii_id, type=5, seq=1, msg=form.message5.data, face=1)
        msg6 = MiiMsgInfo(mii_id=mii_id, type=6, seq=1, msg=form.message6.data, face=1)
        msg7 = MiiMsgInfo(mii_id=mii_id, type=7, seq=1, msg=form.message7.data, face=1)
        # Now to add all of them
        db.session.add(msg1)
        db.session.add(msg2)
        db.session.add(msg3)
        db.session.add(msg4)
        db.session.add(msg5)
        db.session.add(msg6)
        db.session.add(msg7)
        db.session.add(concierge_data)
        db.session.commit()

        update_mii_on_s3(mii_id)
        return redirect(url_for("list_concierge"))
    else:
        # Populate the data
        form.prof.data = mii_msg_infos[0][0].prof
        form.movieid.data = mii_msg_infos[0][0].movie_id
        for _, info in mii_msg_infos:
            if not form[f"message{info.type}"].data:
                form[f"message{info.type}"].data = ""

            # We separate sequencing by newlines.
            if info.seq != 1:
                form[f"message{info.type}"].data += "\n"

            form[f"message{info.type}"].data += info.msg

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

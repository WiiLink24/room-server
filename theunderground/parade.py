import os
import shutil

from flask import render_template, redirect, url_for, send_from_directory
from flask_login import login_required

from room import app
from models import RoomMiis, db
from theunderground.encodemii import parade_encode
from theunderground.forms import ParadeForm
from theunderground.operations import manage_delete_item


@app.route("/theunderground/parade")
@login_required
def list_parade():
    parade_miis = RoomMiis.query.order_by(RoomMiis.mii_id.asc()).all()
    return render_template(
        "parade_list.html", miis=parade_miis, type_length=len(parade_miis)
    )


@app.route("/theunderground/parade/<mii_id>/create", methods=["GET", "POST"])
@login_required
def create_parade(mii_id):
    form = ParadeForm()
    q = RoomMiis.query.filter_by(mii_id=mii_id).first()
    if form.validate_on_submit():

        q = RoomMiis.query.filter_by(mii_id=mii_id)
        if list(q):
            mii = q.first()
            mii.mii_msg = form.mii_msg.data
        else:
            mii = RoomMiis(
                room_id=form.room_id.data,
                mii_id=mii_id,
                mii_msg=form.mii_msg.data,
            )

        db.session.add(mii)
        db.session.commit()

        save_parade_image(form.image.data.read(), mii.room_id)

        return redirect(url_for("list_parade"))

    return render_template("parade_add.html", form=form, room=q)


@app.route("/theunderground/parade/<mii_id>/edit", methods=["GET", "POST"])
@login_required
def edit_parade(mii_id):
    form = ParadeForm()
    q = RoomMiis.query.filter_by(mii_id=mii_id).first()
    if form.validate_on_submit():

        q = RoomMiis.query.filter_by(mii_id=mii_id)
        if list(q):
            mii = q.first()
            mii.mii_msg = form.mii_msg.data
        else:
            mii = RoomMiis(
                room_id=form.room_id.data,
                mii_id=mii_id,
                mii_msg=form.mii_msg.data,
            )

        db.session.add(mii)
        db.session.commit()

        save_parade_image(form.image.data.read(), mii.room_id)

        return redirect(url_for("list_parade"))

    return render_template("parade_edit.html", form=form, room=q)


@app.route("/theunderground/parade/<room_id>/remove", methods=["GET", "POST"])
@login_required
def remove_parade(room_id):
    def drop_parade():
        db.session.delete(RoomMiis.query.filter_by(room_id=room_id).first())
        db.session.commit()
        shutil.rmtree(f"./assets/special/{room_id}")
        return redirect(url_for("list_parade"))

    return manage_delete_item(room_id, "Parade Mii", drop_parade)


@app.route("/theunderground/parade/<room_id>/banner.jpg")
@login_required
def get_parade_banner(room_id):
    return send_from_directory(f"assets/special/{room_id}", "parade_banner.jpg")


def save_parade_image(data: bytes, room_id: int):
    # Create the holding assets folder if it does not already exist.
    if not os.path.isdir(f"./assets/special/{room_id}"):
        os.mkdir(f"./assets/special/{room_id}")

    image_data = parade_encode(data)
    image = open(f"./assets/special/{room_id}/parade_banner.jpg", "wb")
    image.write(image_data)
    image.close()

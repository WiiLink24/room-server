import os
import shutil

from flask import render_template, redirect, url_for, send_from_directory
from flask_login import login_required
from werkzeug import exceptions

from models import db, Rooms, RoomMiis
from theunderground.encodemii import room_logo_encode, parade_encode
from theunderground.forms import RoomForm
from room import app
from theunderground.operations import manage_delete_item


@app.route("/theunderground/rooms")
@login_required
def list_room():
    rooms = Rooms.query.order_by(Rooms.room_id.asc()).all()
    return render_template(
        "room_list.html", rooms=rooms, type_length=len(rooms), type_max_count=30
    )


@app.route("/theunderground/rooms/edit/<room_id>", methods=["GET", "POST"])
@login_required
def edit_room(room_id):
    form = RoomForm()

    mii = RoomMiis.query.filter_by(room_id=room_id).first()
    if not mii:
        return exceptions.NotFound()

    room = Rooms.query.filter_by(room_id=room_id).first()
    if not room:
        return exceptions.NotFound()

    if form.validate_on_submit():
        # Encode our room logo, if updated.
        if form.room_logo.data:
            save_room_logo(form.parade_banner.data.read(), room_id)

        # Save the parade image, if updated.
        if form.parade_banner.data:
            save_parade_image(form.parade_banner.data.read(), room_id)

        mii.mii_id = form.mii.data
        mii.mii_msg = form.mii_msg.data
        db.session.add(mii)
        db.session.commit()

        room.bgm = form.bgm.data
        room.mascot = form.has_mascot.data
        room.contact = form.has_contact.data
        room.intro_msg = form.intro_msg.data
        room.contact_data = form.contact.data
        room.news = form.news.data
        db.session.add(room)
        db.session.commit()

        return redirect(url_for("list_room"))
    else:
        # Populate our form.
        # This is long and unwieldy...
        form.mii.data = mii.mii_id
        form.mii_msg.data = mii.mii_msg
        form.bgm.data = room.bgm
        form.has_mascot.data = room.mascot
        form.has_contact.data = room.contact
        form.intro_msg.data = room.intro_msg
        form.contact.data = room.contact_data
        form.news.data = room.news

    return render_template(
        "room_action.html", form=form, room_id=room_id, action="Edit"
    )


@app.route("/theunderground/rooms/create", methods=["GET", "POST"])
@login_required
def create_room():
    form = RoomForm()
    form.parade_banner.flags.required = True
    form.room_logo.flags.required = True

    if form.validate_on_submit():
        # First, add our room. Auto-increment will give us a
        # room ID to associate images and Miis with.
        room = Rooms(
            bgm=form.bgm.data,
            mascot=form.has_mascot.data,
            contact=form.has_contact.data,
            intro_msg=form.intro_msg.data,
            contact_data=form.contact.data,
            news=form.news.data,
        )
        db.session.add(room)
        db.session.commit()

        # Next, handle room data - our room logo, and parade banner.
        save_room_logo(form.room_logo.data.read(), room.room_id)
        save_parade_image(form.parade_banner.data.read(), room.room_id)

        # Finally, add our Mii.
        mii = RoomMiis(
            room_id=room.room_id,
            mii_id=form.mii.data,
            mii_msg=form.mii_msg.data,
        )
        db.session.add(mii)
        db.session.commit()

        return redirect(url_for("list_room"))

    return render_template("room_action.html", form=form, action="Create")


@app.route("/theunderground/rooms/<room_id>/remove", methods=["GET", "POST"])
@login_required
def remove_room(room_id):
    def drop_room():
        db.session.delete(RoomMiis.query.filter_by(room_id=room_id).first())
        db.session.delete(Rooms.query.filter_by(room_id=room_id).first())
        db.session.commit()
        shutil.rmtree(f"./assets/special/{room_id}")
        return redirect(url_for("list_room"))

    return manage_delete_item(room_id, "room", drop_room)


@app.route("/theunderground/rooms/<room_id>/banner.jpg")
@login_required
def get_room_logo(room_id):
    return send_from_directory(f"./assets/special/{room_id}/", "f1234.img")


@app.route("/theunderground/rooms/<room_id>/parade_banner.jpg")
@login_required
def get_parade_banner(room_id):
    return send_from_directory(f"assets/special/{room_id}", "parade_banner.jpg")


def get_room_dir(room_id: int) -> str:
    path = f"./assets/special/{room_id}"

    if not os.path.exists(path):
        os.makedirs(path)

    return path


def save_parade_image(data: bytes, room_id: int):
    room_dir = get_room_dir(room_id)
    image_data = parade_encode(data)
    image = open(f"{room_dir }/parade_banner.jpg", "wb")
    image.write(image_data)
    image.close()


def save_room_logo(data: bytes, room_id: int):
    room_dir = get_room_dir(room_id)
    image_data = room_logo_encode(data)
    image = open(f"{room_dir }/f1234.img", "wb")
    image.write(image_data)
    image.close()

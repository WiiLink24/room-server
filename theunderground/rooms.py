import shutil

from flask import render_template, redirect, url_for

from werkzeug import exceptions

from asset_data import RoomLogoAsset, ParadeBannerAsset, NormalCategoryAsset
from models import db, Rooms, RoomMiis
from theunderground.forms import RoomForm
from room import app, s3
from theunderground.operations import manage_delete_item
from theunderground.admin import oidc
import config


@app.route("/theunderground/rooms")
@oidc.require_login
def list_room():
    rooms = Rooms.query.order_by(Rooms.room_id.asc()).all()
    return render_template(
        "room_list.html", rooms=rooms, type_length=len(rooms), type_max_count=30
    )


@app.route("/theunderground/rooms/edit/<room_id>", methods=["GET", "POST"])
@oidc.require_login
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
            RoomLogoAsset(room.room_id).encode(form.room_logo)

        # Save the parade image, if updated.
        if form.parade_banner.data:
            ParadeBannerAsset(room.room_id).encode(form.parade_banner)

        if form.category_logo.data:
            NormalCategoryAsset(room.room_id + 30000).encode(form.category_logo)

        mii.mii_id = form.mii.data
        mii.mii_msg = form.mii_msg.data
        db.session.add(mii)
        db.session.commit()

        room.bgm = form.bgm.data
        room.mascot = form.has_mascot.data
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
        form.intro_msg.data = room.intro_msg
        form.contact.data = room.contact_data
        form.news.data = room.news

    rooms = Rooms.query.order_by(Rooms.room_id.asc()).all()

    return render_template(
        "room_action.html", form=form, room_id=room_id, action="Edit", rooms=rooms
    )


@app.route("/theunderground/rooms/create", methods=["GET", "POST"])
@oidc.require_login
def create_room():
    form = RoomForm()
    form.parade_banner.flags.required = True
    form.room_logo.flags.required = True
    form.category_logo.flags.required = True

    if form.validate_on_submit():
        # First, add our room. Auto-increment will give us a
        # room ID to associate images and Miis with.
        room = Rooms(
            bgm=form.bgm.data,
            mascot=form.has_mascot.data,
            intro_msg=form.intro_msg.data,
            contact_data=form.contact.data,
            news=form.news.data,
        )
        db.session.add(room)
        db.session.commit()

        # Next, add our Mii.
        mii = RoomMiis(
            room_id=room.room_id,
            mii_id=form.mii.data,
            mii_msg=form.mii_msg.data,
        )
        db.session.add(mii)
        db.session.commit()

        # Finally, handle room data - our room logo, and parade banner.
        RoomLogoAsset(room.room_id).encode(form.room_logo)
        ParadeBannerAsset(room.room_id).encode(form.parade_banner)
        NormalCategoryAsset(room.room_id + 30000).encode(form.category_logo)

        return redirect(url_for("list_room"))

    return render_template("room_action.html", form=form, action="Create")


@app.route("/theunderground/rooms/<room_id>/remove", methods=["GET", "POST"])
@oidc.require_login
def remove_room(room_id):
    def drop_room():
        db.session.delete(RoomMiis.query.filter_by(room_id=room_id).first())
        db.session.delete(Rooms.query.filter_by(room_id=room_id).first())
        db.session.commit()
        shutil.rmtree(f"./assets/special/{room_id}")
        NormalCategoryAsset(room_id + 30000).delete()

        if s3:
            # Delete from S3
            ParadeBannerAsset(room_id).remove_from_s3()

        return redirect(url_for("list_room"))

    return manage_delete_item(room_id, "room", drop_room)


@app.route("/theunderground/rooms/<room_id>/banner.jpg")
@oidc.require_login
def get_room_logo(room_id):
    if s3:
        return redirect(f"{config.url1_cdn_url}/special/{room_id}/img/f1234.img")

    return RoomLogoAsset(room_id).send_file()


@app.route("/theunderground/rooms/<room_id>/parade_banner.jpg")
@oidc.require_login
def get_parade_banner(room_id):
    if s3:
        return redirect(f"{config.url1_cdn_url}/special/{room_id}/img/g1234.img")

    return ParadeBannerAsset(room_id).send_file()


@app.route("/theunderground/rooms/<int:room_id>/category_logo.jpg")
@oidc.require_login
def get_category_logo(room_id):
    return NormalCategoryAsset(room_id + 30000).send_file()

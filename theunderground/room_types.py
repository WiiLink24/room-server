from io import BytesIO

from flask import render_template, redirect, url_for, flash
from theunderground.admin import oidc

from room import app, s3
from models import RoomMenu, db

from theunderground.forms import (
    PreRoomData,
    RoomDeliveryData,
    RoomVoteData,
    RoomMovieData,
    RoomLinkData,
    RoomPicData,
)
from theunderground.mobiclip import validate_mobiclip
from url1.special import room_content_types as tv
from url1.special.page import special_page_n
from theunderground.room_paths import (
    save_delivery_data,
    save_vote_data,
    save_mov_data,
    save_link_data,
    save_pic_data,
)

import config


@app.route("/theunderground/rooms/<room_id>/choose", methods=["GET", "POST"])
@oidc.require_login
def choose_type(room_id):
    form = PreRoomData()

    if form.validate_on_submit():
        value = form.type.data

        if value == "Delivery":
            return redirect(url_for("delivery", room_id=room_id))

        if value == "Poll":
            return redirect(url_for("poll", room_id=room_id))

        if value == "Movie":
            return redirect(url_for("movie", room_id=room_id))

        # TODO: Figure out coupons for Dokodemo
        if value == "Coupon":
            return redirect(url_for("root"))

        if value == "Link":
            return redirect(url_for("link", room_id=room_id))

        if value == "Picture":
            return redirect(url_for("pic", room_id=room_id))

    return render_template("room_type_choose.html", form=form)


# In order for rooms to have different photos and movies, both their respective id's and photo_id
# must be different. These functions query the database for the last value then adds by 1.
def x_id():
    num = RoomMenu.query.order_by(RoomMenu.id.desc()).first()
    if num is not None:
        return num.id + 1
    else:
        return 1


def photo_id():
    num = RoomMenu.query.order_by(RoomMenu.id.desc()).first()
    if num is not None:
        proper_id = int(num.data["imageid"][1:]) + 1

        return proper_id
    else:
        return 1000


@app.route("/theunderground/rooms/<room_id>/add/delivery", methods=["GET", "POST"])
@oidc.require_login
def delivery(room_id):
    form = RoomDeliveryData()

    if form.validate_on_submit():
        movie = form.movie.data
        image = form.image.data
        thumbnail = form.tv.data
        if movie and image:
            movie_data = movie.read()
            image_data = image.read()
            tv_data = thumbnail.read()

            if validate_mobiclip(movie_data):
                db_json = RoomMenu(
                    room_id=room_id, data=tv.smp(photo_id(), x_id(), form.title.data)
                )

                # Since the photo ID and ID are pulled from the db, committing before
                # saving the files will cause mismatched file names.
                save_delivery_data(
                    x_id(), movie_data, image_data, tv_data, photo_id(), room_id
                )

                db.session.add(db_json)
                db.session.commit()

                save_page_xml_to_s3(room_id)
                return redirect(url_for("list_room_data", room_id=room_id))
            else:
                flash("Invalid movie!")
        else:
            flash("Error uploading movie!")

    return render_template("room_add_delivery.html", form=form)


@app.route("/theunderground/rooms/<room_id>/add/poll", methods=["GET", "POST"])
@oidc.require_login
def poll(room_id):
    form = RoomVoteData()

    if form.validate_on_submit():
        image1 = form.image1.data
        image2 = form.image2.data
        image3 = form.image3.data
        thumbnail = form.tv.data
        if thumbnail and image1:
            image1_data = image1.read()
            image2_data = image2.read()
            image3_data = image3.read()
            thumbnail_data = thumbnail.read()

            db_json = RoomMenu(
                room_id=room_id,
                data=tv.enq(
                    photo_id(),
                    x_id(),
                    form.question.data,
                    form.title.data,
                    form.mii_msg.data,
                ),
            )

            save_vote_data(
                image1_data,
                image2_data,
                image3_data,
                thumbnail_data,
                photo_id(),
                room_id,
            )

            db.session.add(db_json)
            db.session.commit()

            save_page_xml_to_s3(room_id)
            return redirect(url_for("list_room_data", room_id=room_id))
        else:
            flash("Error uploading movie!")

    return render_template("room_add_vote.html", form=form)


@app.route("/theunderground/rooms/<room_id>/add//mov", methods=["GET", "POST"])
@oidc.require_login
def movie(room_id):
    form = RoomMovieData()

    if form.validate_on_submit():
        image = form.image.data
        if image:
            image_data = image.read()

            db_json = RoomMenu(
                room_id=room_id,
                data=tv.mov(photo_id(), form.movie_id.data, form.title.data),
            )

            save_mov_data(photo_id(), image_data, room_id)

            db.session.add(db_json)
            db.session.commit()

            save_page_xml_to_s3(room_id)
            return redirect(url_for("list_room_data", room_id=room_id))
        else:
            flash("Error uploading movie!")

    return render_template("room_add_mov.html", form=form)


@app.route("/theunderground/rooms/<room_id>/add/link", methods=["GET", "POST"])
@oidc.require_login
def link(room_id):
    form = RoomLinkData()

    if form.validate_on_submit():
        movie = form.movie.data
        thumbnail = form.tv.data
        image1 = form.image1.data
        image2 = form.image2.data
        if movie and tv:
            movie_data = movie.read()
            tv_data = thumbnail.read()
            image1_data = image1.read()
            image2_data = image2.read()
            if validate_mobiclip(movie_data):
                db_json = RoomMenu(
                    room_id=room_id,
                    data=tv.link(
                        photo_id(),
                        x_id(),
                        form.title.data,
                        form.link.data,
                        form.bgm.data.value,
                    ),
                )

                save_link_data(
                    x_id(),
                    movie_data,
                    image1_data,
                    image2_data,
                    tv_data,
                    photo_id(),
                    room_id,
                )

                db.session.add(db_json)
                db.session.commit()

                save_page_xml_to_s3(room_id)
                return redirect(url_for("list_room_data", room_id=room_id))
            else:
                flash("Invalid movie!")
        else:
            flash("Error uploading movie!")

    return render_template("room_add_link.html", form=form)


@app.route("/theunderground/rooms/<room_id>/add/pic", methods=["GET", "POST"])
@oidc.require_login
def pic(room_id):
    form = RoomPicData()

    if form.validate_on_submit():
        thumbnail = form.tv.data
        image1 = form.image1.data
        image2 = form.image2.data
        image3 = form.image3.data
        if tv:
            tv_data = thumbnail.read()
            image1_data = image1.read()
            image2_data = image2.read()
            image3_data = image3.read()

            db_json = RoomMenu(
                room_id=room_id,
                data=tv.pic(
                    photo_id(),
                    x_id(),
                    form.title.data,
                    form.bgm.data.value,
                ),
            )

            save_pic_data(
                image1_data,
                image2_data,
                image3_data,
                tv_data,
                x_id(),
                photo_id(),
                room_id,
            )

            db.session.add(db_json)
            db.session.commit()

            save_page_xml_to_s3(room_id)
            return redirect(url_for("list_room_data", room_id=room_id))
        else:
            flash("Error uploading picture!")

    return render_template("room_add_pic.html", form=form)


def save_page_xml_to_s3(page_id: int):
    if s3:
        page_xml = special_page_n(page_id)
        s3.upload_fileobj(
            BytesIO(page_xml), config.r2_bucket_name, f"special/{page_id}/page.xml"
        )

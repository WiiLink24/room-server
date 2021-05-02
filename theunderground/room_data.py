from flask import render_template, redirect, url_for, flash
from flask_login import login_required

from room import app, db
from models import RoomMenu

from theunderground.forms import (
    PreRoomData,
    RoomDeliveryData,
    RoomVoteData,
    RoomMovieData,
    RoomLinkData,
)
from theunderground.mobiclip import validate_mobiclip
from url1.special import room_content_types as tv
from theunderground.room_paths import (
    save_delivery_data,
    save_vote_data,
    save_mov_data,
    save_link_data,
)


@app.route("/theunderground/roomtype/choose", methods=["GET", "POST"])
@login_required
def choose_type():
    form = PreRoomData()

    if form.validate_on_submit():
        value = form.type.data
        print(value)

        if value == "Delivery":
            return redirect(url_for("delivery"))

        if value == "Poll":
            return redirect(url_for("poll"))

        if value == "Movie":
            return redirect(url_for("movie"))

        if value == "Coupon":
            return redirect(url_for("root"))

        if value == "Link":
            return redirect(url_for("root"))

        if value == "Picture":
            return redirect(url_for("root"))

    return render_template("choose_room_type.html", form=form)


# In order for rooms to have different photos and movies, both their respective id's and photo_id
# must be different. These functions query the database for the last value then adds by 1 or 1234.
def room_id():
    num = RoomMenu.query.order_by(RoomMenu.id.desc()).first()

    return num.id + 1


def photo_id():
    num = RoomMenu.query.order_by(RoomMenu.id.desc()).first()

    return num.id + 1234


@app.route("/theunderground/roomtype/delivery", methods=["GET", "POST"])
@login_required
def delivery():
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
                db_json = RoomMenu(data=tv.smp(photo_id(), room_id(), form.title.data))

                # Since the photo ID and ID are pulled from the db, committing before
                # saving the files will cause mismatched file names.
                save_delivery_data(id(), movie_data, image_data, tv_data, photo_id())

                db.session.add(db_json)
                db.session.commit()

                return redirect(url_for("root"))
            else:
                flash("Invalid movie!")
        else:
            flash("Error uploading movie!")

    return render_template("room_add_delivery.html", form=form)


@app.route("/theunderground/roomtype/poll", methods=["GET", "POST"])
@login_required
def poll():
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
                data=tv.enq(
                    photo_id(),
                    room_id(),
                    form.question.data,
                    form.title.data,
                    form.mii_msg.data,
                )
            )

            save_vote_data(
                image1_data, image2_data, image3_data, thumbnail_data, photo_id()
            )

            db.session.add(db_json)
            db.session.commit()

            return redirect(url_for("root"))
        else:
            flash("Error uploading movie!")

    return render_template("room_add_vote.html", form=form)


@app.route("/theunderground/roomtype/mov", methods=["GET", "POST"])
@login_required
def movie():
    form = RoomMovieData()

    if form.validate_on_submit():
        image = form.image.data
        if image:
            image_data = image.read()

            db_json = RoomMenu(
                data=tv.mov(photo_id(), form.movie_id.data, form.title.data)
            )

            save_mov_data(photo_id(), image_data)

            db.session.add(db_json)
            db.session.commit()

            return redirect(url_for("root"))
        else:
            flash("Error uploading movie!")

    return render_template("room_add_mov.html", form=form)


@app.route("/theunderground/roomtype/link", methods=["GET", "POST"])
@login_required
def link():
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
                    data=tv.link(
                        photo_id(),
                        room_id(),
                        form.title.data,
                        form.link.data,
                        form.bgm.data.value,
                    )
                )

                save_link_data(
                    room_id(), movie_data, image1_data, image2_data, tv_data, photo_id()
                )

                db.session.add(db_json)
                db.session.commit()

                return redirect(url_for("root"))
            else:
                flash("Invalid movie!")
        else:
            flash("Error uploading movie!")

    return render_template("room_add_link.html", form=form)

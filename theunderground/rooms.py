import os

from flask import render_template, redirect, url_for, flash, send_from_directory
from flask_login import login_required

from models import Rooms
from room import app, db
from theunderground.encodemii import room_logo
from theunderground.forms import KillMii, RoomForm
from room import app
from theunderground.forms import RoomMovieForm
from models import RoomMenu


@app.route("/theunderground/rooms/<id>/movie", methods=["GET", "POST"])
@login_required
def roommovie(id):
    form = RoomMovieForm()
    if form.validate_on_submit():
        movie_id = form.movie_id.data
        place = form.place.data
        imageid = form.imageid.data
        title = form.title.data
        data = {
            "type": 3,
            "imageid": imageid,
            "mov": {"movieid": movie_id, "title": title},
        }
        menu = RoomMenu(room_id=id, data=data)
        db.session.add(menu)
        db.session.commit()
        return redirect(url_for(f"theunderground/rooms/{id}"))
    return render_template("room_movie.html", form=form)


@app.route("/theunderground/rooms/<id>/link", methods=["GET", "POST"])
@login_required
def roomlink(id):
    form = RoomLinkForm()
    if form.validate_on_submit():
        place = form.place.data
        title = form.title.data
        imageid = form.imageid.data
        url = form.url.data
        linkid = form.linkid.data
        data = {
            "type": 5,
            "imageid": imageid,
            "link": {
                "linkid": movie_id,
                "linktitle": title,
                "linktype": 0,
                "linkmov": 0,
                "linkpicnum": 1,
                "linkurl": url,
                "linkpicbgm": 1,
            },
        }
        menu = RoomMenu(room_id=id, data=data)
        db.session.add(menu)
        db.session.commit()
        return redirect(url_for(f"theunderground/rooms/{id}"))
    return render_template("add_link.html", form=form)


@app.route("/theunderground/rooms")
@login_required
def list_room():
    rooms = Rooms.query.order_by(Rooms.room_id.asc()).all()
    return render_template("room_list.html", rooms=rooms)


@app.route("/theunderground/rooms/<room_id>", methods=["GET", "POST"])
@login_required
def edit_room(room_id):
    form = RoomForm()

    if form.validate_on_submit():
        # Encode an image to the appropriate size.
        room_image = room_logo(form.room_logo.data.read())
        # Save to our assets directory.
        path = get_room_dir(room_id) + "/f1234.img"
        file = open(path, "wb")
        file.write(room_image)
        file.close()

        room = Rooms.query.filter_by(room_id=room_id).first()
        if room:
            room.bgm = form.bgm.data
            room.mascot = form.has_mascot.data
            room.contact = form.has_contact.data
            room.intro_msg = form.intro_msg.data
            room.mii_msg = form.mii_msg.data
        else:
            room = Rooms(
                room_id=room_id,
                bgm=form.bgm.data,
                mascot=form.has_mascot.data,
                contact=form.has_contact.data,
                intro_msg=form.intro_msg.data,
                mii_msg=form.mii_msg.data,
                logo2_id="f1234",
            )

        db.session.add(room)
        db.session.commit()
        return redirect(url_for("/theunderground/rooms/"))

    return render_template("room_edit.html", form=form)


@app.route("/theunderground/rooms/<room_id>/remove", methods=["GET", "POST"])
@login_required
def remove_room(room_id):
    form = KillMii()
    if form.validate_on_submit():
        # While this is easily circumvented, we need the user to pay attention.
        if form.given_mii_id.data == room_id:
            db.session.delete(Rooms.query.filter_by(room_id=room_id).first())
            db.session.commit()
            return redirect(url_for("list_room"))
        else:
            flash("Incorrect room ID!")
    return render_template("room_delete.html", form=form, room_id=room_id)


@app.route("/theunderground/rooms/<room_id>/banner.jpg")
@login_required
def get_room_logo(room_id):
    room = Rooms.query.filter_by(room_id=room_id).first()
    asset_id = room.logo2_id

    return send_from_directory("assets/special-" + room_id, f"{asset_id}.img")


def get_room_dir(room_id: int) -> str:
    path = f"./assets/special-{room_id}"

    if not os.path.exists(path):
        os.mkdir(path)

    return path

import os
import config

from flask import (
    render_template,
    redirect,
    flash,
    send_from_directory,
    request,
    url_for,
)
from flask_login import login_required
from flask_wtf.file import FileRequired
from werkzeug import exceptions

from asset_data import NormalCategoryAsset, RoomLogoAsset
from models import Categories, Movies, EvaluateData, RoomMenu, Rooms, db
from room import app, s3
from theunderground.forms import CategoryForm
from theunderground.operations import manage_delete_item
from theunderground.mobiclip import (
    get_category_list,
    validate_mobiclip,
    get_mobiclip_length,
    save_movie_data,
    delete_movie_data,
    get_movie_path,
)

@app.route("/theunderground/enquete")
def enquete_room_list():
    rooms = Rooms.query.order_by(Rooms.room_id.asc()).all()
    return render_template(
        "enquete_room_list.html", rooms=rooms, type_length=len(rooms), type_max_count=30
    )

@app.route("/theunderground/enquete/<room_id>")
def enquete_room_data(room_id):
    data = RoomMenu.query.filter_by(room_id=room_id).all()

    # Iterate through the data so we can replace the type numbers with their names
    for tv in data:
        if tv.data["type"] == 1:
            tv.data["type"] = "Delivery"

        elif tv.data["type"] == 2:
            tv.data["type"] = "Voting"

        elif tv.data["type"] == 3:
            tv.data["type"] = "Movie"

        elif tv.data["type"] == 4:
            tv.data["type"] = "Coupon"

        elif tv.data["type"] == 5:
            tv.data["type"] = "Website Link"

        elif tv.data["type"] == 6:
            tv.data["type"] = "Picture"

    return render_template(
        "enquete_room_data.html", datas=data, type_length=len(data), room_id=room_id
    )

@app.route("/theunderground/enquete/<room_id>/banner.jpg")
def enquete_get_room_logo(room_id):
    if s3:
        return redirect(f"{config.url1_cdn_url}/special/{room_id}/img/f1234.img")

    return RoomLogoAsset(room_id).send_file()

@app.route("/theunderground/enquete/<room_id>/TV/<image_id>.jpg")
def enquete_room_data_image(room_id, image_id):
    if s3:
        return redirect(f"{config.url1_cdn_url}/special/{room_id}/img/{image_id}.img")

    return send_from_directory(f"./assets/special/{room_id}", image_id + ".img")
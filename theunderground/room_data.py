import os
import config

from room import app, s3

from flask import render_template, send_from_directory, redirect, url_for
from models import RoomMenu, db
from theunderground.operations import manage_delete_item
from theunderground.admin import oidc
from theunderground.logging import log_action


@app.route("/theunderground/rooms/<room_id>")
@oidc.require_login
def list_room_data(room_id):
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
        "room_data_list.html", datas=data, type_length=len(data), room_id=room_id
    )


@app.route(
    "/theunderground/rooms/<room_id>/remove/<data_id>/<image_id>",
    methods=["GET", "POST"],
)
@oidc.require_login
def remove_tv_item(room_id, data_id, image_id):
    def drop_tv_item():
        db.session.delete(RoomMenu.query.filter_by(id=data_id).first())
        db.session.commit()
        os.remove(f"./assets/special/{room_id}/{image_id}.img")

        log_action(f"Content {data_id} for room {room_id} was removed")
        return redirect(url_for("list_room_data", room_id=room_id))

    return manage_delete_item(data_id, "Room Data", drop_tv_item)


@app.route("/theunderground/rooms/<room_id>/TV/<image_id>.jpg")
@oidc.require_login
def serve_room_data_image(room_id, image_id):
    if s3:
        return redirect(f"{config.url1_cdn_url}/special/{room_id}/img/{image_id}.img")

    return send_from_directory(f"./assets/special/{room_id}", image_id + ".img")

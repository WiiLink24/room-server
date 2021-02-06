# Handles pages and logo images
from werkzeug import exceptions

from helpers import current_date_and_time, RepeatedElement, xml_node_name
from models import Room, MiiData
from room import app, db
from flask import send_from_directory


@app.route("/url1/special/<page>/page.xml")
@xml_node_name("SpPage")
def special_page_n(page):
    query = (
        db.session.query(Room, MiiData)
        .filter(Room.room_id == page)
        .filter(Room.room_id == MiiData.mii_id)
        .first()
    )

    if not query:
        return exceptions.NotFound()

    queried_room, queried_mii = query

    return {
        "sppageid": page,
        # TODO: database schema should handle proper times regarding catalog.
        "strdt": current_date_and_time(),
        "enddt": current_date_and_time(),
        "name": queried_room.room_name,
        "stopflag": 0,
        "level": 1,
        "bgm": queried_room.bgm.value,
        "mascot": queried_room.mascot,
        "contact": queried_room.contact,
        "intro": {
            "inmsginfo": {
                "inmsgseq": 1,
                "inmsg": queried_room.intro_msg,
            }
        },
        "miiinfo": {
            "seq": 1,
            "miiid": queried_mii.mii_id,
            "color1": queried_mii.color1,
            "color2": queried_mii.color2,
            "msginfo": [
                RepeatedElement(
                    {
                        "msgseq": 1,
                        "msg": queried_room.mii_msg,
                    }
                ),
            ],
        },
        "menu": {
            "place": 1,
            "type": 4,
            "imageid": "d1234",
            "coup": {
                "coupid": 1,
                "couptitle": "coupon test",
                "couplimit": 10,
                "coupmov": 1,
                "coupmovap": 0,
            },
        },
        "logo": {"logo1id": queried_room.logo1_id, "logo2id": queried_room.logo2_id},
    }


if app.debug:

    @app.route("/url1/special/<page>/img/<img>")
    def handle_img(page, img):
        # Handles logo images, for instance:
        # GET /url1/special/1/img/g1234.img
        # Gets g1234.img
        return send_from_directory("assets/special-" + page, img)

# Handles pages and logo images
from werkzeug import exceptions

from helpers import current_date_and_time, RepeatedElement, xml_node_name
from models import Rooms, MiiData, ParadeMiis, RoomMenu
from room import app, db
from flask import send_from_directory


@app.route("/url1/special/<page>/page.xml")
@xml_node_name("SpPage")
def special_page_n(page):
    query = (
        db.session.query(Rooms, MiiData, ParadeMiis)
        .filter(Rooms.room_id == page)
        .filter(Rooms.room_id == MiiData.mii_id)
        .filter(Rooms.room_id == ParadeMiis.mii_id)
        .first()
    )

    if not query:
        return exceptions.NotFound()

    queried_room, queried_mii, queried_parade = query
    menu_data = db.session.query(RoomMenu).filter(RoomMenu.room_id == page).all()

    menus = []
    for place, data in enumerate(menu_data):
        menus.append(RepeatedElement(data.data | {"place": place + 1}))

    return {
        "sppageid": page,
        # TODO: database schema should handle proper times regarding catalog.
        "strdt": current_date_and_time(),
        "enddt": current_date_and_time(),
        "name": queried_parade.news,
        "stopflag": 0,
        "level": queried_parade.level,
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
        "menu": menus,
        "logo": {"logo1id": queried_parade.logo_id, "logo2id": queried_room.logo2_id},
    }


@app.route("/url1/special/0/page.xml")
@xml_node_name("SpPage")
def page_0():
    # TODO: revert from temporary, pre-determined value to database schema
    intro_filler = []
    for i in range(9):
        intro_filler.append(
            RepeatedElement(
                {
                    "inmsgseq": i + 1,
                    "inmsg": "Hello!",
                }
            )
        )

    msginfo_filler = []
    for i in range(3):
        msginfo_filler.append(
            RepeatedElement(
                {
                    "msgseq": i + 1,
                    "msg": "Testing...",
                }
            )
        )

    return {
        "sppageid": "0",
        # TODO: database schema should handle proper times regarding catalog.
        "strdt": current_date_and_time(),
        "enddt": current_date_and_time(),
        "name": "Testing: The Movie",
        "stopflag": 0,
        "level": 1,
        "bgm": 2,
        "mascot": 0,
        "contact": 0,
        "intro": {"inmsginfo": intro_filler},
        "miiinfo": {
            "seq": 1,
            "miiid": 1,
            "color1": "ffcd00",
            "color2": "000000",
            "msginfo": msginfo_filler,
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
        "logo": {"logo1id": "g1234", "logo2id": "f1234"},
    }


if app.debug:
    @app.route("/url1/special/<page>/img/<img>")
    def handle_img(page, img):
        # Handles logo images, for instance:
        # GET /url1/special/1/img/g1234.img
        # Gets g1234.img
        return send_from_directory("assets/special-" + page, img)


    @app.route("/url1/urllink/<movie_id>.mov")
    def handle_urllink(movie_id):
        # Handles movies for room type "link"
        return send_from_directory("assets/urllink", movie_id + ".mov")

    @app.route("/url1/urllink/<movie_id>.img")
    def handle_urlink(movie_id):
        # Handles movies for room type "link"
        return send_from_directory("assets/urllink", movie_id + ".img")

    @app.route("/url1/urllink/<movie_id>.mov")
    def handle_picture(movie_id):
        # Handles movies for room type "link"
        return send_from_directory("assets/picture", movie_id + ".mov")

    @app.route("/url1/delivery/<movie_id>.mov")
    def handle_delivery(movie_id):
        # Handles movies for room type "link"
        return send_from_directory("assets/delivery", movie_id + ".mov")

    @app.route("/url1/delivery/<img>.img")
    def handle_deliveryimg(img):
        # Handles logo images, for instance:
        # GET /url1/special/1/img/g1234.img
        # Gets g1234.img
        return send_from_directory("assets/delivery", img + ".img")

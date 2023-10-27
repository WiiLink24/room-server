# Handles pages and logo images
from werkzeug import exceptions

from asset_data import ParadeBannerAsset
from helpers import current_date_and_time, RepeatedElement, xml_node_name
from models import Rooms, MiiData, RoomMenu, RoomMiis, db
from room import app
from flask import send_from_directory


@app.route("/url1/special/<page>/page.xml")
@xml_node_name("SpPage")
def special_page_n(page):
    query = (
        db.session.query(Rooms, RoomMiis, MiiData)
        .filter(Rooms.room_id == page)
        .filter(Rooms.room_id == RoomMiis.room_id)
        .filter(RoomMiis.mii_id == MiiData.mii_id)
        .first()
    )

    if not query:
        return exceptions.NotFound()

    room_data, room_mii, mii_data = query
    menu_data = db.session.query(RoomMenu).filter(RoomMenu.room_id == page).all()

    menus = [
        RepeatedElement(data.data | {"place": place + 1})
        for place, data in enumerate(menu_data)
    ]
    return {
        "sppageid": page,
        # TODO: database schema should handle proper times regarding catalog.
        "strdt": current_date_and_time(),
        "enddt": current_date_and_time(),
        "name": room_data.news,
        "stopflag": 0,
        "level": room_data.level,
        "bgm": room_data.bgm.value,
        "mascot": room_data.mascot,
        # If we have contact data, we should enable contacting.
        "contact": room_data.contact_data is not None,
        "intro": {
            "inmsginfo": {
                "inmsgseq": 1,
                "inmsg": room_data.intro_msg,
            }
        },
        "miiinfo": {
            "seq": 1,
            "miiid": mii_data.mii_id,
            "color1": mii_data.color1,
            "color2": mii_data.color2,
            "msginfo": [
                RepeatedElement(
                    {
                        "msgseq": 1,
                        "msg": room_mii.mii_msg,
                    }
                ),
            ],
        },
        "menu": menus,
        "logo": {
            # We hardcode all parade logo IDs to g1234.
            "logo1id": "g1234",
            # Similarly, all room IDs are f1234.
            "logo2id": "f1234",
        },
    }


@app.route("/url1/special/0/page.xml")
@xml_node_name("SpPage")
def page_0():
    return {
        "sppageid": "0",
        "strdt": current_date_and_time(),
        "enddt": current_date_and_time(),
        "name": "Secret",
        "stopflag": 0,
        "level": 1,
        "bgm": 2,
        "mascot": 0,
        "contact": 0,
        "intro": {
            "inmsginfo": {
                "inmsgseq": 1,
                "inmsg": "Hello from the WiiLink24 Team!",
            }
        },
        "miiinfo": {
            "seq": 1,
            "miiid": 1,
            "color1": "ffcd00",
            "color2": "000000",
            "msginfo": [
                RepeatedElement(
                    {
                        "msgseq": 1,
                        "msg": "This room exists so movies function.",
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
                "couptitle": "Coupon test!",
                "couplimit": 10,
                "coupmov": 1,
                "coupmovap": 0,
            },
        },
        "logo": {"logo1id": "g1234", "logo2id": "f1234"},
    }


if app.debug:

    @app.route("/url1/special/<room_id>/img/g1234.img")
    def handle_parade_banner(room_id):
        return ParadeBannerAsset(room_id).send_file()

    @app.route("/url1/special/<page>/img/<img>")
    def handle_img(page, img):
        return send_from_directory(f"assets/special/{page}", img)

    @app.route("/url1/urllink/<movie_id>.mov")
    def handle_urllink(movie_id):
        # Handles movies for room type "link"
        return send_from_directory("assets/urllink", f"{movie_id}.mov")

    @app.route("/url1/urllink/<movie_id>.img")
    def handle_urlink(movie_id):
        # Handles movies for room type "link"
        return send_from_directory("assets/urllink", f"{movie_id}.img")

    @app.route("/url1/picture/<movie_id>")
    def handle_picture(movie_id):
        # Handles movies for room type "pic"
        return send_from_directory("assets/picture", movie_id)

    @app.route("/url1/delivery/<movie_id>.mov")
    def handle_delivery(movie_id):
        # Handles movies for room type "delivery"
        return send_from_directory("assets/delivery", f"{movie_id}.mov")

    @app.route("/url1/delivery/<img>.img")
    def handle_deliveryimg(img):
        # Handles movies for room type "delivery"
        return send_from_directory("assets/delivery", f"{img}.img")

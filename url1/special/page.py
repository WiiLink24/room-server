# Handles pages and logo images
from werkzeug import exceptions

from asset_data import ParadeBannerAsset
from helpers import current_date_and_time, RepeatedElement, xml_node_name
from models import Rooms, MiiData, RoomMenu, RoomMiis, db
from room import app
from flask import send_from_directory
from textwrap import wrap


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

    menus = []
    for place, data in enumerate(menu_data):
        menus.append(RepeatedElement(data.data | {"place": place + 1}))

    intro_msgs = []
    for i, msg in enumerate(room_data.intro_msg.split("\n")):
        intro_msgs.append(
            RepeatedElement(
                {
                    "inmsgseq": i + 1,
                    "inmsg": "\n".join(wrap(msg, 23)),
                }
            )
        )

    mii_msgs = []
    for i, msg in enumerate(room_mii.mii_msg.split("\n")):
        mii_msgs.append(
            RepeatedElement({"msgseq": i + 1, "msg": "\n".join(wrap(msg, 23))})
        )

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
        "intro": {"inmsginfo": intro_msgs},
        "miiinfo": {
            "seq": 1,
            "miiid": mii_data.mii_id,
            "color1": mii_data.color1,
            "color2": mii_data.color2,
            "msginfo": mii_msgs,
        },
        "menu": menus,
        "logo": {
            # We hardcode all parade logo IDs to g1234.
            "logo1id": "g1234",
            # Similarly, all room IDs are f1234.
            "logo2id": "f1234",
        },
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
        return send_from_directory("assets/urllink", movie_id + ".mov")

    @app.route("/url1/urllink/<movie_id>.img")
    def handle_urlink(movie_id):
        # Handles movies for room type "link"
        return send_from_directory("assets/urllink", movie_id + ".img")

    @app.route("/url1/picture/<movie_id>")
    def handle_picture(movie_id):
        # Handles movies for room type "pic"
        return send_from_directory("assets/picture", movie_id)

    @app.route("/url1/delivery/<movie_id>.mov")
    def handle_delivery(movie_id):
        # Handles movies for room type "delivery"
        return send_from_directory("assets/delivery", movie_id + ".mov")

    @app.route("/url1/delivery/<img>.img")
    def handle_deliveryimg(img):
        # Handles movies for room type "delivery"
        return send_from_directory("assets/delivery", img + ".img")

    @app.route("/url1/coupon/<movie_id>.mov")
    def handle_coupon_movie(movie_id):
        return send_from_directory("assets/coupon", movie_id + ".mov")

    @app.route("/url1/coupon/<movie_id>-W.img")
    def handle_coupon_image(movie_id):
        return send_from_directory("assets/coupon", movie_id + "-W.img")

    @app.route("/url1/coupon/<movie_id>.enc")
    def handle_coupon(movie_id):
        return send_from_directory("assets/coupon", movie_id + ".enc")

    @app.route("/url1/special/<page>/mascot.bin")
    def handle_mascot(page):
        return send_from_directory(f"assets/special/{page}", "mascot.bin")

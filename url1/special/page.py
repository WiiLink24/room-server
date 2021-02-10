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
    menu_data = db.session.query(RoomMenu).filter(Rooms.room_id == page).all()
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
        "menu": menu,
        "logo": {"logo1id": queried_parade.logo_id, "logo2id": queried_room.logo2_id},
    }


if app.debug:

    @app.route("/url1/special/<page>/img/<img>")
    def handle_img(page, img):
        # Handles logo images, for instance:
        # GET /url1/special/1/img/g1234.img
        # Gets g1234.img
        return send_from_directory("assets/special-" + page, img)

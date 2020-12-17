# Handles pages and logo images
from helpers import current_date_and_time, RepeatedElement, xml_node_name
from room import app
from flask import send_from_directory


@app.route("/url1/special/<page>/page.xml")
@xml_node_name("SpPage")
def special_page_n(page):
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
        "sppageid": page,
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
    "menu":{
        "place": 1,
        "type": 4,
        "imageid": 'd1234',
        "coup":{
            "coupid":1,
            "couptitle": "coupon test",
            "couplimit":10,
            "coupmov":0,
            "coupmovap":0,
        }
    }
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

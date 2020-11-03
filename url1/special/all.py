from room import app
from helpers import current_date_and_time, xml_node_name, RepeatedElement


@app.route("/url1/special/all.xml")
@xml_node_name("SpPageList")
def special_all():
    return {
        "pageinfo": [
            RepeatedElement(
                {
                    "sppageid": 1,
                    "name": "Testing",
                    "level": 1,
                    "miiid": 1,
                    "color1": "111111",
                    "color2": "222222",
                    "logo1id": "g1234",
                    "news": "Testing...",
                    "valid": 1,
                    "pref": "11111111111111111111111111111111111111111111111",
                }
            ),
            RepeatedElement(
                {
                    "sppageid": 2,
                    "name": "Testing",
                    "level": 1,
                    "miiid": 1,
                    "color1": "111111",
                    "color2": "222222",
                    "logo1id": "g1234",
                    "news": "Testing...",
                    "valid": 1,
                    "pref": "11111111111111111111111111111111111111111111111",
                }
            ),
            RepeatedElement(
                {
                    "sppageid": 3,
                    "name": "Testing",
                    "level": 1,
                    "miiid": 1,
                    "color1": "111111",
                    "color2": "222222",
                    "logo1id": "g1234",
                    "news": "Testing...",
                    "valid": 1,
                    "pref": "11111111111111111111111111111111111111111111111",
                }
            ),
        ],
        "upddt": current_date_and_time(),
    }

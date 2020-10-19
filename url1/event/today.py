from collections import OrderedDict

from room import app
from helpers import current_date, xml_node_name, RepeatedKey


@app.route("/url1/event/today.xml")
@xml_node_name("Event")
def event_today():
    return {
        "date": current_date(),
        "frameid": 2,
        "color": "000000",
        "postertime": 5,
        "posterinfo": {
            "seq": 1,
            "posterid": 1,
        },
        "miiinfo": {
            "seq": 1,
            "miiid": 1,
        },
        "newsinfo": {"page": 1, "news": "Welcome to Wii Room."},
        "adinfo": (
            RepeatedKey(
                {
                    "pref": 2,
                    "adid": 1,
                }
            ),
            RepeatedKey(
                {
                    "pref": 1,
                    "adid": 1,
                }
            ),
        ),
        "introinfo": {
            "seq": 1,
            "cntid": 1,
            "cnttype": 1,
            "dispsec": 5,
            "dimg": 1,
            "random": 0,
            "linktype": 0,
        },
    }

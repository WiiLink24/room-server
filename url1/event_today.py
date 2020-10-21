from sqlalchemy import asc

from room import app
from helpers import current_date, xml_node_name, RepeatedElement, RepeatedKey
from models import Posters


@app.route("/url1/event/today.xml")
@xml_node_name("Event")
def event_today():
    # Retrieve all registered posters.
    queried_posters = Posters.query.order_by(asc(Posters.poster_id)).limit(20).all()
    # Create a dictionary and append contents.
    # We require separate posterinfos, so we use RepeatedElement.
    posters = []
    miiinfos = []
    for seq, poster in enumerate(queried_posters):
        posters.append(
            RepeatedElement(
                {
                    # Seq is indexed by 1, whereas a normal index is 0.
                    "seq": seq + 1,
                    "posterid": poster.poster_id,
                }
            )
        )
    for seq, mii in enumerate(queried_posters):
        miiinfos.append(
            RepeatedElement(
                {
                    "seq": seq + 1,
                    "miiid": mii.miiid
                }
            )
        )

    return {
        "date": current_date(),
        "frameid": 2,
        "color": "000000",
        "postertime": 5,
        "posterinfo": posters,
        "miiinfo": miiinfos,
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

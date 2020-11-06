from flask import send_from_directory

from room import app
from helpers import current_date, xml_node_name, RepeatedElement
from models import PayPosters


@app.route("/url3/pay/event/today.xml")
@xml_node_name("Event")
def pay_event_today():
    # Retrieve all registered posters.
    queried_posters = (
        PayPosters.query.order_by(PayPosters.poster_id.asc()).limit(20).all()
    )

    posters = []
    for seq, poster in enumerate(queried_posters):
        posters.append(
            RepeatedElement(
                {
                    "seq": seq + 1,
                    "posterid": poster.poster_id,
                    "geofilter": 0,
                }
            )
        )

    return {
        "date": current_date(),
        "postertime": 5,
        "posterinfo": posters,
        "introinfo": {
            "seq": 1,
            "cntid": 1,
            "cnttype": 1,
            "dispsec": 5,
            "dimg": 1,
            "random": 0,
            "linktype": 5,
            "linkid": 1,
        },
    }


if app.debug:

    @app.route("/url3/pay/intro/<name>.img")
    def serve_pay_intro(name):
        return send_from_directory("assets/pay-intro", name + ".img")

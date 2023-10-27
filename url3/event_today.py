from flask import send_from_directory

from room import app
from helpers import current_date, xml_node_name, RepeatedElement, is_v770
from models import PayPosters, Categories


@app.route("/url3/pay/event/today.xml")
@xml_node_name("Event")
def pay_event_today():
    # Retrieve all registered posters.
    queried_posters = (
        PayPosters.query.order_by(PayPosters.poster_id.asc()).limit(20).all()
    )

    if is_v770:
        return pay_event_today_v770(queried_posters)
    else:
        return pay_event_today_v1025(queried_posters)


def pay_event_today_v1025(queried_posters):
    posters = [
        RepeatedElement(
            {
                "seq": seq + 1,
                "posterid": poster.poster_id,
                "geofilter": 0,
            }
        )
        for seq, poster in enumerate(queried_posters)
    ]
    # In order to avoid hardcoding a category ID, we get the
    # first category's ID.
    first_category = Categories.query.order_by(Categories.category_id.asc()).first()

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
            "linkid": first_category.category_id,
        },
    }


def pay_event_today_v770(queried_posters):
    poster_id_one = queried_posters[0].poster_id
    poster_id_two = queried_posters[1].poster_id

    return {
        "date": current_date(),
        "postertime": 5,
        "posterid1": poster_id_one,
        "posterid2": poster_id_two,
        "introinfo": {
            "seq": 1,
            # Movie IDs must be 16 digits.
            "intromovid": "1".rjust(16, "0"),
            "linktype": 1,
            "movieid": 1,
        },
    }


if app.debug:

    @app.route("/url3/pay/intro/<name>.img")
    def serve_pay_intro(name):
        return send_from_directory("assets/pay-intro", f"{name}.img")

    @app.route("/url3/pay/intro/<movie_id>.mov")
    def serve_pay_intro_movie(movie_id):
        return send_from_directory("assets/pay-intro", f"{movie_id}.mov")

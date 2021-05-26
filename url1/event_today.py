from flask import send_from_directory

from room import app
from helpers import current_date, xml_node_name, RepeatedElement, RepeatedKey, is_v770
from models import Posters, ConciergeMiis, News


@app.route("/url1/event/today.xml")
@xml_node_name("Event")
def event_today():
    # Retrieve all registered posters.
    queried_posters = Posters.query.order_by(Posters.poster_id.asc()).limit(20).all()
    queried_miis = (
        ConciergeMiis.query.order_by(ConciergeMiis.mii_id.asc()).limit(20).all()
    )
    # Create a dictionary and append contents.
    # We require separate posterinfos, so we use RepeatedElement.
    posters = []
    miiinfos = []
    newsinfos = []
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

    for seq, mii in enumerate(queried_miis):
        miiinfos.append(RepeatedElement({"seq": seq + 1, "miiid": mii.mii_id}))
    for page, news in enumerate(News.query.order_by(News.id).all()):
        newsinfos.append(RepeatedElement({"page": page + 1, "news": news.msg}))

    return_dict = {
        "date": current_date(),
        "frameid": 2,
        "color": "000000",
        "postertime": 5,
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

    if is_v770:
        # v770 expects only one poster.
        # As we've already queried the DB, insert the first poster.
        poster_id = posters[0].contents["posterid"]
        return_dict["posterid"] = poster_id

        # Additionally, ads are sideways on v770. We'll only have one ad ID.
        return_dict["adinfo"] = (
            RepeatedKey(
                {
                    "pref": 2,
                    "adid": 1000001,
                }
            ),
            RepeatedKey(
                {
                    "pref": 1,
                    "adid": 1000001,
                }
            ),
        )
    else:
        # v1025 expects multiple posters, similar to how we've queried.
        return_dict["posterinfo"] = posters

    if newsinfos:
        return_dict["newsinfo"] = newsinfos

    if miiinfos:
        return_dict["miiinfo"] = miiinfos

    return return_dict


if app.debug:

    @app.route("/url1/intro/<name>.img")
    def serve_intro(name):
        return send_from_directory("assets/normal-intro", name + ".img")

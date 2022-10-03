from flask import send_from_directory

from room import app
from helpers import current_date, xml_node_name, RepeatedElement, RepeatedKey, is_v770
from models import Posters, ConciergeMiis, News, IntroInfo, ContentTypes, LinkTypes


@app.route("/url1/event/today.xml")
@xml_node_name("Event")
def event_today():
    # Retrieve all registered posters.
    queried_posters = Posters.query.order_by(Posters.poster_id.asc()).limit(20).all()
    queried_miis = (
        ConciergeMiis.query.order_by(ConciergeMiis.mii_id.asc()).limit(20).all()
    )
    queried_intro_info = IntroInfo.query.order_by(IntroInfo.cnt_id.asc()).all()
    # Create a dictionary and append contents.
    # We require separate posterinfos, so we use RepeatedElement.
    posters = []
    miiinfos = []
    newsinfos = []
    introinfos = []
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
    for seq, info in enumerate(queried_intro_info):
        data = {
            "seq": seq + 1,
            "cntid": info.cnt_id,
            "cnttype": info.cnt_type.value,
            "random": 0,
            "linktype": info.link_type.value,
        }

        if info.cnt_type == ContentTypes.Image:
            data["dispsec"] = 5
            data["dimg"] = 1

        if info.link_type != LinkTypes.Regular:
            data["linkid"] = info.link_id

        if info.cat_name:
            data["catname"] = info.cat_name

        introinfos.append(RepeatedElement(data))

    return_dict = {
        "date": current_date(),
        "frameid": 100000,
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

    if introinfos:
        return_dict["introinfo"] = introinfos

    if newsinfos:
        return_dict["newsinfo"] = newsinfos

    if miiinfos:
        return_dict["miiinfo"] = miiinfos

    return return_dict


if app.debug:

    @app.route("/url1/intro/<name>.img")
    def serve_intro(name):
        return send_from_directory("assets/normal-intro", name + ".img")

    @app.route("/url1/intro/<name>.mov")
    def serve_intro_movie(name):
        return send_from_directory("assets/normal-intro", name + ".mov")

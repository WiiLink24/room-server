from asset_data import TVScreenAsset
from flask import send_from_directory

from room import app
from helpers import (
    current_date,
    xml_node_name,
    RepeatedElement,
    RepeatedKey,
    is_v770,
    wii_locale,
)
from models import Posters, ConciergeMiis, News, IntroInfo, ContentTypes, LinkTypes, db
import os
import config
import random


def set_current_community_photo():
    """As of June 2026, the first image seen when loading up Wii Room will be one uploaded by the community
    in the Discord server. We cycle through selected images every 24h at random."""
    with app.app_context():
        photos = os.listdir(config.community_photos_dir)
        if len(photos) == 0:
            # Empty, do nothing
            return

        # Pick at random
        photo_name = random.choice(photos)

        full_path = os.path.join(config.community_photos_dir, photo_name)

        # Copy for every locale.
        first_intro_infos = (
            db.session.query(IntroInfo).where(IntroInfo.position == 1).all()
        )

        photo_bytes = None
        with open(full_path, "rb") as photo:
            photo_bytes = photo.read()
        print(full_path)
        for info in first_intro_infos:
            # Encode and write image
            TVScreenAsset(info.cnt_id, is_theatre=False, is_movie=False).encode(
                photo_bytes
            )


@app.route("/url1/event/today.xml")
@xml_node_name("Event")
def event_today():
    # Retrieve all registered posters.
    queried_posters = (
        db.session.query(Posters)
        .where(Posters.locale == wii_locale)
        .order_by(Posters.poster_id.asc())
        .limit(20)
        .all()
    )
    queried_miis = (
        db.session.query(ConciergeMiis)
        .where(ConciergeMiis.locale == wii_locale)
        .order_by(ConciergeMiis.mii_id.asc())
        .limit(20)
        .all()
    )
    queried_intro_info = (
        db.session.query(IntroInfo)
        .where(IntroInfo.locale == wii_locale)
        .order_by(IntroInfo.position.asc())
        .all()
    )
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
    for info in queried_intro_info:
        data = {
            "seq": info.position,
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
        "frameid": 1000001,
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

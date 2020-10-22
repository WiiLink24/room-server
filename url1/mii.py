from werkzeug import exceptions

from room import app
from helpers import xml_node_name, RepeatedKey, RepeatedElement, current_date_and_time
from models import Miis, MiiData, MiiMsgInfo


@app.route("/url1/mii/<int:mii_id>.mii")
def mii_met(mii_id):
    # Do we have this Mii?
    mii = MiiData.query.filter_by(mii_id=mii_id).first()
    if mii is None:
        return exceptions.NotFound()

    data = mii.data
    # Ensure this Mii has a CRC-16, i.e that is is 76 bytes stored and not 74 as normal.
    if len(data) != 76:
        print(f"Mii #{mii_id} lacks a CRC-16 checksum. Was it inserted properly?")
        return exceptions.InternalServerError()

    return mii.data


@app.route("/url1/mii/<int:mii_id>.met")
@xml_node_name("ConciergeMii")
def obtain_mii(mii_id):
    # Do we have this Mii?
    mii_metadata = Miis.query.filter_by(mii_id=mii_id).first()
    if mii_metadata is None:
        return exceptions.NotFound()

    # Next, ensure we have msginfo data for this Mii.
    db_msginfo = (
        MiiMsgInfo.query.filter_by(mii_id=mii_id)
        .order_by(MiiMsgInfo.type.asc())
        .order_by(MiiMsgInfo.seq.asc())
    )
    if db_msginfo is None:
        print(f"Mii #{mii_id} lacks msginfo data. Was it inserted properly?")
        return exceptions.NotFound()

    # Separate by type and seq.
    # We create a dict where the key is the type and seq/msg are paired by RepeatedKey.
    # We're given in order by type, and then by seq.
    # i.e 1 seq 1, 1 seq 2, 2 seq 1, so forth.
    separate = {}
    for info in db_msginfo:
        if info.type not in separate:
            # Ensure the list exists within the dict.
            separate[info.type] = []

        # As seq/msg can repeat within a single msginfo, we add with a RepeatedKey.
        separate[info.type].append(
            RepeatedElement({"seq": info.seq, "msg": info.msg, "face": info.face})
        )

    # Then, convert all separate types to our actual msginfo type.
    # In these, the type (our previous dict's key) must be separate.
    # This is absolutely horrifying at this point, and I do not envy
    # whoever at Nintendo had to design and store this logic.
    # For the sake of their sanity, I hope this was read off a giant
    # hardcoded array somehow as that feels far more appealing.
    msginfo = []
    for key, value in separate.items():
        msginfo.append(RepeatedElement({"type": key, "msglist": value}))

    return {
        "miiid": mii_id,
        "clothes": mii_metadata.clothes,
        "color1": mii_metadata.color1,
        "color2": mii_metadata.color2,
        "action": mii_metadata.action,
        "prof": mii_metadata.prof,
        "name": mii_metadata.name,
        "msginfo": msginfo,
        "movieid": mii_metadata.movie_id,
        "upddt": current_date_and_time(),
    }

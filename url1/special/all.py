from models import MiiData, Rooms, RoomMiis
from room import app, db
from helpers import current_date_and_time, xml_node_name, RepeatedElement


@app.route("/url1/special/all.xml")
@xml_node_name("SpPageList")
def special_all():
    page_info = []

    parade_miis = (
        db.session.query(Rooms, RoomMiis, MiiData)
        .filter(Rooms.room_id == RoomMiis.room_id)
        .filter(RoomMiis.mii_id == MiiData.mii_id)
        .order_by(RoomMiis.room_id)
        .all()
    )

    for room_data, room_mii, mii_data in parade_miis:
        page_info.append(
            RepeatedElement(
                {
                    "sppageid": room_data.room_id,
                    "name": mii_data.name,
                    "level": room_data.level,
                    "miiid": mii_data.mii_id,
                    "color1": mii_data.color1,
                    "color2": mii_data.color2,
                    # We hardcode all parade logo IDs to g1234.
                    "logo1id": "g1234",
                    "news": room_data.news,
                    "valid": 1,
                    "pref": "11111111111111111111111111111111111111111111111",
                }
            )
        )

    return {
        "pageinfo": page_info,
        "upddt": current_date_and_time(),
    }

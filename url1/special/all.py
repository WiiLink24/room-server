from models import MiiData, Rooms, db
from room import app
from helpers import current_date_and_time, xml_node_name, RepeatedElement, wii_locale


@app.route("/url1/special/all.xml")
@xml_node_name("SpPageList")
def special_all():
    page_info = []

    parade_miis = (
        db.session.query(Rooms, MiiData)
        .where(Rooms.locale == wii_locale)
        .filter(Rooms.parade_mii == MiiData.mii_id)
        .order_by(Rooms.room_id)
        .all()
    )

    for room_data, mii_data in parade_miis:
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

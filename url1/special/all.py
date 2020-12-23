from models import ParadeMiis, MiiData
from room import app, db
from helpers import current_date_and_time, xml_node_name, RepeatedElement


@app.route("/url1/special/all.xml")
@xml_node_name("SpPageList")
def special_all():
    page_info = []

    parade_miis = (
        db.session.query(ParadeMiis, MiiData)
        .filter(ParadeMiis.mii_id == MiiData.mii_id)
        .order_by(ParadeMiis.mii_id)
        .all()
    )

    for parade_mii, mii_data in parade_miis:
        page_info.append(
            RepeatedElement(
                {
                    "sppageid": parade_mii.sppageid,
                    "name": mii_data.name,
                    "level": parade_mii.level,
                    "miiid": mii_data.mii_id,
                    "color1": mii_data.color1,
                    "color2": mii_data.color2,
                    "logo1id": parade_mii.logo_id,
                    "news": parade_mii.news,
                    "valid": 1,
                    "pref": "11111111111111111111111111111111111111111111111",
                }
            )
        )

    return {
        "pageinfo": page_info,
        "upddt": current_date_and_time(),
    }

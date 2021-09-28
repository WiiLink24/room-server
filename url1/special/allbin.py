from helpers import xml_node_name, RepeatedElement
from room import app, db
from models import ParadeMiis, MiiData, Rooms


@app.route("/url1/special/allbin.xml")
@xml_node_name("SpPageBin")
def special_allbin():
    bin_info = []

    # Join queries. We select all ParadeMii data alongside MiiData table data with equal Mii IDs.
    # TODO: determine maximum limit we can select and return.
    parade_miis = (
        db.session.query(ParadeMiis, MiiData, Rooms)
        .filter(ParadeMiis.mii_id == MiiData.mii_id)
        .filter(ParadeMiis.mii_id == Rooms.mii_id)
        .order_by(ParadeMiis.mii_id)
        .all()
    )

    # We now have a tuple with ParadeMii data in index 0 and MiiData in index 1.
    for parade_mii, mii_data, room_data in parade_miis:
        bin_info.append(
            RepeatedElement(
                {
                    "sppageid": room_data.room_id,
                    "miiid": mii_data.mii_id,
                    "miibin": mii_data.data,
                    "logo1id": parade_mii.logo_id,
                    "logobin": parade_mii.logo_bin,
                }
            )
        )

    return {
        "bininfo": bin_info,
    }

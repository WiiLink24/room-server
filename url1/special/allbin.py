from asset_data import ParadeBannerAsset
from helpers import xml_node_name, RepeatedElement
from room import app
from models import MiiData, Rooms, db


@app.route("/url1/special/allbin.xml")
@xml_node_name("SpPageBin")
def special_allbin():
    bin_info = []

    # Join queries. We select all ParadeMii data alongside MiiData table data with equal Mii IDs.
    parade_miis = (
        db.session.query(Rooms, MiiData)
        .filter(Rooms.parade_mii == MiiData.mii_id)
        .order_by(Rooms.room_id)
        .limit(30)
        .all()
    )

    for room_data, mii_data in parade_miis:
        # Read the parade banner image for this room ID.
        room_id = room_data.room_id

        with ParadeBannerAsset(room_id).asset_path().open("rb") as asset:
            parade_banner = asset.read()

        bin_info.append(
            RepeatedElement(
                {
                    "sppageid": room_id,
                    "miiid": mii_data.mii_id,
                    "miibin": mii_data.data,
                    # We hardcode all parade logo IDs to g1234.
                    "logo1id": "g1234",
                    "logobin": parade_banner,
                }
            )
        )

    return {
        "bininfo": bin_info,
    }

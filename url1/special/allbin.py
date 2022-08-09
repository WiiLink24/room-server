from asset_data import ParadeBannerAsset
from helpers import xml_node_name, RepeatedElement
from room import app
from models import MiiData, Rooms, RoomMiis, db


@app.route("/url1/special/allbin.xml")
@xml_node_name("SpPageBin")
def special_allbin():
    bin_info = []

    # Join queries. We select all ParadeMii data alongside MiiData table data with equal Mii IDs.
    # TODO: determine maximum limit we can select and return.
    queried_data = (
        db.session.query(Rooms, RoomMiis, MiiData)
        .filter(Rooms.room_id == RoomMiis.room_id)
        .filter(RoomMiis.mii_id == MiiData.mii_id)
        .order_by(RoomMiis.room_id)
        .all()
    )

    for room_data, room_mii, mii_data in queried_data:
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

from models import Categories, Rooms, ConciergeMiis, MiiData
from room import app, db
from helpers import xml_node_name, RepeatedElement, wii_locale


@app.route("/url1/list/category/<list_id>.xml")
@xml_node_name("CategoryList")
def list_category_n(list_id):
    # list_id:
    # 01: All
    # 02: Miis
    # 03: Rooms
    results = []
    match list_id:
        case "01":
            queried_categories = (
                db.session.query(Categories)
                .filter(Categories.unlisted == False)
                .where(Categories.locale == wii_locale)
                .order_by(Categories.name.asc())
                .limit(64)
                .all()
            )

            for i, category in enumerate(queried_categories):
                # Items must be indexed by 1.
                results.append(
                    RepeatedElement(
                        {
                            "place": i + 1,
                            "categid": category.category_id,
                            "name": category.name,
                            "sppageid": 0,
                            "splinktext": "Link text",
                        }
                    )
                )
        case "02":
            concierge_miis = (
                db.session.query(ConciergeMiis, MiiData)
                .where(ConciergeMiis.locale == wii_locale)
                .filter(ConciergeMiis.mii_id == MiiData.mii_id)
                .all()
            )

            for i, mii in enumerate(concierge_miis):
                # Items must be indexed by 1.
                results.append(
                    RepeatedElement(
                        {
                            "place": i + 1,
                            # Category ID must be 5 digits.
                            "categid": 20000 + mii[0].mii_id,
                            "name": mii[1].name,
                            # The following are unused in this context.
                            "sppageid": 0,
                            "splinktext": "Placeholder",
                        }
                    )
                )
        case "03":
            queried_data = (
                db.session.query(Rooms)
                .where(Rooms.locale == wii_locale)
                .order_by(Rooms.news.asc())
                .all()
            )
            for i, room in enumerate(queried_data):
                # Items must be indexed by 1.
                results.append(
                    RepeatedElement(
                        {
                            "place": i + 1,
                            "categid": 30000 + room.room_id,
                            "name": room.news,
                            "sppageid": room.room_id,
                            "splinktext": room.news,
                        }
                    )
                )

    return {
        "type": 3,
        "categinfo": results,
    }


if app.debug:

    @app.route("/url1/list/category/img/<category_id>.img")
    def serve_category_images(category_id):
        from asset_data import NormalCategoryAsset

        return NormalCategoryAsset(category_id).send_file()

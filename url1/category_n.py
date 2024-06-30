from models import Categories, Rooms
from room import app, db
from helpers import xml_node_name, RepeatedElement


@app.route("/url1/list/category/<list_id>.xml")
@xml_node_name("CategoryList")
def list_category_n(list_id):
    queried_data = (
        db.session.query(Categories, Rooms)
        .filter(Categories.sp_page_id == Rooms.room_id)
        .order_by(Categories.name.asc())
        .limit(64)
        .all()
    )
    results = []

    for i, category in enumerate(queried_data):
        # Items must be indexed by 1.
        results.append(
            RepeatedElement(
                {
                    "place": i + 1,
                    "categid": category[0].category_id,
                    "name": category[0].name,
                    "sppageid": category[1].room_id,
                    "splinktext": category[1].news,
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

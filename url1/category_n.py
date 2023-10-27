from asset_data import NormalCategoryAsset
from models import Categories
from room import app
from helpers import xml_node_name, RepeatedElement


@app.route("/url1/list/category/<list_id>.xml")
@xml_node_name("CategoryList")
def list_category_n(list_id):
    queried_categories = (
        Categories.query.order_by(Categories.name.asc()).limit(64).all()
    )
    results = [
        RepeatedElement(
            {
                "place": i + 1,
                "categid": category.category_id,
                "name": category.name,
                "sppageid": 0,
                "splinktext": "Link text",
            }
        )
        for i, category in enumerate(queried_categories)
    ]
    return {
        "type": 3,
        "categinfo": results,
    }


if app.debug:

    @app.route("/url1/list/category/img/<category_id>.img")
    def serve_category_images(category_id):
        return NormalCategoryAsset(category_id).send_file()

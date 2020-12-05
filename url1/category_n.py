from flask import send_from_directory

from models import Categories
from room import app
from helpers import xml_node_name, RepeatedElement


@app.route("/url1/list/category/<list_id>.xml")
@xml_node_name("CategoryList")
def list_category_n(list_id):
    # TODO: remove cursed hack for list padding.
    queried_categories = (
        Categories.query.order_by(Categories.name.asc()).limit(64).all()
    )
    results = []

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

    return {
        "type": 3,
        "categinfo": results,
    }


if app.debug:

    @app.route("/url1/list/category/img/<name>.img")
    def serve_category_images(name):
        return send_from_directory("assets/normal-category", name + ".img")

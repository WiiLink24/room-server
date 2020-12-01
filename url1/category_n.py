from flask import send_from_directory

from room import app
from helpers import xml_node_name, RepeatedElement


@app.route("/url1/list/category/<list_id>.xml")
@xml_node_name("CategoryList")
def list_category_n(list_id):
    # TODO: revert from temporary, pre-determined value to database schema
    filler = []
    for i in range(64):
        # Items must be indexed by 1.
        filler.append(
            RepeatedElement(
                {
                    "place": i + 1,
                    "categid": 12345,
                    "name": "Category text",
                    "sppageid": 0,
                    "splinktext": "Link text",
                }
            )
        )

    return {
        "type": 3,
        "categinfo": filler,
    }


if app.debug:

    @app.route("/url1/list/category/img/<name>.img")
    def serve_category_images(name):
        return send_from_directory("assets/normal-category", name + ".img")

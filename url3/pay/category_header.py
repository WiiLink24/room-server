from flask import send_from_directory

from room import app
from helpers import xml_node_name, RepeatedElement


@app.route("/url3/pay/list/category/header.xml")
@xml_node_name("PayCategoryHeader")
def pay_list_category_header():
    # TODO: revert from temporary, pre-determined value to database schema
    filler = []
    for i in range(40):
        # Items must be indexed by 1.
        filler.append(
            RepeatedElement(
                {
                    "place": i + 1,
                    "type": i + 10,
                    "text": "Testing...",
                }
            )
        )

    return {
        "img": 0,
        "listinfo": filler,
    }


if app.debug:

    @app.route("/url3/pay/list/category/img/<name>.img")
    def serve_pay_category_images(name):
        return send_from_directory("assets/pay-category", name + ".img")

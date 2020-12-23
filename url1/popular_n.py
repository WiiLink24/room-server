from room import app
from helpers import xml_node_name, RepeatedElement, current_date_and_time


@app.route("/url1/list/popular/<id>.xml")
@xml_node_name("Popular")
def popular_n(id):
    # TODO: revert from temporary, pre-determined value to database schema
    filler = []
    for i in range(3):
        # Items must be indexed by 1.
        filler.append(
            RepeatedElement(
                {
                    "place": i + 1,
                    "categid": 12345,
                    "name": "Category text",
                    "sppageid": 1,
                    "splinktext": "Link text",
                }
            )
        )

    response = {
        "type": 1,
        "categinfo": filler,
    }
    # The ID 02 requires a type of 3.
    if id == "02":
        response["type"] = 3

    return response

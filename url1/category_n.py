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

from room import app
from helpers import xml_node_name
@xml_node_name("PayCategoryList")
@app.route("/url3/pay/list/category/{id}.xml")
def pay_list_category_list(id):
    # TODO: revert from temporary, pre-determined value to database schema
    filler = []
    for i in range(64):
        # Items must be indexed by 1.
        filler.append(
            RepeatedElement(
                {
                    "place": i + 1,
                    "categid":12345,
                    "name": "Testing...",
                    "sppageid": 0,
                    "splinktext": "Link Text"
                }
            )
        )

    return {
        "type":id[2],
        "img": 0,
        "categinfo": filler,
    }


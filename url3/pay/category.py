from room import app
from helpers import xml_node_name, RepeatedElement
from models import PayCategories


@app.route("/url3/pay/list/category/<list_id>.xml")
@xml_node_name("PayCategoryList")
def pay_list_category(list_id):
    queried_categories = PayCategories.query.order_by(PayCategories.name.asc()).all()
    filler = []
    for i, pay_categories in enumerate(queried_categories):
        # Items must be indexed by 1.
        filler.append(
            RepeatedElement(
                {
                    "place": i + 1,
                    "categid": pay_categories.category_id,
                    "name": pay_categories.name,
                    "sppageid": 0,
                    "splinktext": "Link Text",
                }
            )
        )

    return {
        "type": 3,
        "img": 0,
        "categinfo": filler,
    }



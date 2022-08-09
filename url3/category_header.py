from room import app
from helpers import xml_node_name, RepeatedElement
from models import PayCategoryHeaders


@app.route("/url3/pay/list/category/header.xml")
@xml_node_name("PayCategoryHeader")
def pay_list_category_header():
    queried_categories = PayCategoryHeaders.query.order_by(
        PayCategoryHeaders.title.asc()
    ).all()
    filler = []
    for i, pay_category_headers in enumerate(queried_categories):
        # Titles must be indexed by 1.
        filler.append(
            RepeatedElement(
                {
                    "place": i + 1,
                    "type": i + 10,
                    "text": pay_category_headers.title,
                }
            )
        )

    return {
        "img": 0,
        "listinfo": filler,
    }

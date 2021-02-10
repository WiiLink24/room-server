from room import app
from helpers import xml_node_name, RepeatedElement
from models import PayCategories


@app.route("/url3/pay/list/category/<list_id>.xml")
@xml_node_name("PayCategoryList")
def pay_list_category(list_id):
    queried_categories = (
        PayCategories.query.order_by(PayCategories.name.asc()).all()
    )
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


@app.route("/url3/pay/list/category/search/<category>")
@xml_node_name("SearchMovies")
def search_movies(category):
    return {
        "num": 1,
        "categid": category,
        "movieinfo": {
            "rank": 1,
            "movieid": 123,
            "title": "doggo",
            "strdt": "2020-10-10T01:11:11",
            "pop": 0,
            "kana": 12345678,
            "refid": "01234567890123456789012345678912",
            "released": "2020-10-10",
            "term": 1,
            "price": 0,
        },
    }

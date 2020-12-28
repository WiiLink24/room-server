from room import app
from helpers import xml_node_name, RepeatedElement
@app.route("/url3/pay/list/category/03.xml")
@xml_node_name("PayCategoryList")
def pay_list_category_list():
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
        "type":3,
        "img": 0,
        "categinfo": filler,
    }

@app.route("/url3/pay/list/category/search/<category>')
@xml_node_name("SearchMovies")
def search_movies(category):
    return {
        "num":1,
        "categid":category,
        "movieinfo":{
            "rank":1,
            "movieid":123,
            "title":"doggo",
            "strdt":"2020-10-10T01:11:11",
            "pop":0,
            "kana":12345678,
            "refid":"01234567890123456789012345678912",
            "released":"2020-10-10",
            "term":1,
            "price":0
        }
    }

from room import app
from helpers import xml_node_name, RepeatedElement, current_date_and_time


@app.route("/url1/list/category/search/<categ_id>")
@xml_node_name("SearchMovies")
def list_category_n(categ_id):
    # TODO: revert from temporary, pre-determined value to database schema
    filler = []
    for i in range(3):
        # Items must be indexed by 1.
        filler.append(
            RepeatedElement(
                {
                    "rank": i + 1,
                    "movieid": 1,
                    "title": "Shiba: The Movie",
                    "genre": 1,
                    "strdt": current_date_and_time(),
                    "pop": 0,
                }
            )
        )

    return {
        "num": 1,
        "categid": categ_id,
        "movieinfo": filler,
    }

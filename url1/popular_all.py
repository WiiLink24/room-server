from room import app
from helpers import xml_node_name, RepeatedElement, current_date_and_time
from url2.reginfo import getzone

@app.route("/url1/list/popular/all.xml")
@xml_node_name("Popular")
def popular_all():
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
                    "strdt": getzone(),
                    "pop": 0,
                }
            )
        )

    return {
        "movieinfo": filler,
    }

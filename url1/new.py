from room import app
from helpers import xml_node_name, RepeatedElement
from models import NewMovies
from url2.reginfo import getzone

@app.route("/url1/list/new/all.xml")
@xml_node_name("New")
def new_all():
    queried_categories = NewMovies.query.order_by(NewMovies.title.asc()).all()
    filler = []
    for i, new_movies in enumerate(queried_categories):
        # Items must be indexed by 1.
        filler.append(
            RepeatedElement(
                {
                    "rank": i + 1,
                    "movieid": new_movies.movie_id,
                    "title": new_movies.title,
                    "genre": 1,
                    "strdt": getzone(),
                    "pop": 0,
                }
            )
        )

    return {
        "movieinfo": filler,
    }

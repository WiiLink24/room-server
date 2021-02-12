from room import app
from helpers import xml_node_name, RepeatedElement, current_date_and_time
from models import NewMovies


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
                    "strdt": current_date_and_time(),
                    "pop": 0,
                }
            )
        )

    return {
        "movieinfo": filler,
    }

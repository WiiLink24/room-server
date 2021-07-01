from werkzeug import exceptions

from models import Movies
from room import app
from helpers import xml_node_name, RepeatedElement, current_date_and_time


@app.route("/url1/list/category/search/<categ_id>")
@xml_node_name("SearchMovies")
def list_category_search(categ_id):
    retrieved_data = (
        Movies.query.filter(Movies.category_id == categ_id)
        .order_by(Movies.date_added.desc())
        .all()
    )
    results = []

    if not retrieved_data:
        # Looks like this category does not exist, or contains no movies.
        return exceptions.NotFound()

    for i, movie_data in enumerate(retrieved_data):
        # Items must be indexed by 1.
        results.append(
            RepeatedElement(
                {
                    "rank": i + 1,
                    "movieid": movie_data.movie_id,
                    "title": movie_data.title,
                    "genre": movie_data.genre,
                    "strdt": current_date_and_time(),
                    "pop": 0,
                }
            )
        )

    return {
        "num": 1,
        "categid": categ_id,
        "movieinfo": results,
    }

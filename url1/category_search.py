from werkzeug import exceptions

from models import CategoryMovies, Movies
from room import app, db
from helpers import xml_node_name, RepeatedElement
from url2.reginfo import getzone

@app.route("/url1/list/category/search/<categ_id>")
@xml_node_name("SearchMovies")
def list_category_search(categ_id):
    retrieved_data = (
        db.session.query(CategoryMovies, Movies)
        .filter(CategoryMovies.category_id == categ_id)
        .filter(CategoryMovies.movie_id == Movies.movie_id)
        .order_by(Movies.movie_id)
        .all()
    )
    results = []

    if not retrieved_data:
        # Looks like this category does not exist, or contains no movies.
        return exceptions.NotFound()

    for i, data in enumerate(retrieved_data):
        _, movie_data = data

        # Items must be indexed by 1.
        results.append(
            RepeatedElement(
                {
                    "rank": i + 1,
                    "movieid": movie_data.movie_id,
                    "title": movie_data.title,
                    "genre": movie_data.genre,
                    "strdt": getzone(),
                    "pop": 0,
                }
            )
        )

    return {
        "num": 1,
        "categid": categ_id,
        "movieinfo": results,
    }

from werkzeug import exceptions

from models import Movies, ConciergeMovies, Rooms
from room import app
from helpers import xml_node_name, RepeatedElement, current_date_and_time


@app.route("/url1/list/category/search/<int:categ_id>")
@xml_node_name("SearchMovies")
def list_category_search(categ_id):
    if categ_id < 20000:
        retrieved_data = (
            Movies.query.filter(Movies.category_id == categ_id)
            .filter(Movies.unlisted == False)
            .order_by(Movies.date_added.desc())
            .limit(100)
            .all()
        )
    elif 20000 <= categ_id <= 29999:
        # Concierge Movies
        retrieved_data = (
            Movies.query.filter(Movies.movie_id == ConciergeMovies.movie_id)
            .filter(ConciergeMovies.mii_id == categ_id - 20000)
            .filter(Movies.unlisted == False)
            .order_by(Movies.date_added.desc())
            .limit(100)
            .all()
        )
    else:
        retrieved_data = (
            Movies.query.filter(Movies.sp_page_id == Rooms.room_id)
            .filter(Rooms.room_id == categ_id - 30000)
            .filter(Movies.unlisted == False)
            .order_by(Movies.date_added.desc())
            .limit(100)
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
                    "genre": movie_data.genre.value,
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

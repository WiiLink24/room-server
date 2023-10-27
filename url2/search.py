from flask import request
from helpers import xml_node_name, RepeatedElement, iso_date_and_time
from models import Movies
from room import app

EMPTY_RESPONSE = {"num": 1, "categid": 12345}


@app.route("/url2/search.cgi")
@xml_node_name("SearchMovies")
def general_search():
    q = request.args.get("q")
    if q is None:
        return EMPTY_RESPONSE

    movies = Movies.query.search(q).limit(64).all()

    if movie_infos := [
        RepeatedElement(
            {
                "rank": rank,
                "movieid": movie.movie_id,
                "title": movie.title,
                "genre": movie.genre,
                "strdt": iso_date_and_time(movie.date_added),
                "pop": 0,
            }
        )
        for rank, movie in enumerate(movies, start=1)
    ]:
        return {"num": 1, "categid": 12345, "movieinfo": movie_infos}
    else:
        return {"num": 1, "categid": 12345}

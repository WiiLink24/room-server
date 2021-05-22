from flask import request
from werkzeug import exceptions

from models import Movies
from room import app, db
from helpers import xml_node_name, RepeatedElement


@app.route("/url2/miiinfo.cgi", methods=["GET", "POST"])
@xml_node_name("MiiInfo")
def miiinfo():
    return {"code": 0, "msg": "thanks"}


@app.route("/url2/related.cgi")
@xml_node_name("RelatedMovies")
def related():
    movie = request.args.get("movieid")
    category_result = Movies.query.filter_by(movie_id=movie).first()
    if category_result is None:
        return exceptions.NotFound()

    category_id = category_result.category_id

    movies = (
        Movies.query.filter(Movies.category_id == category_id)
        .order_by(Movies.date_added)
        .limit(15)
        .all()
    )

    movie_info = []

    # The rank must start at 1 for unknown reasons.
    # Our loop will increment it before using it as a rank.
    rank = 0

    for movie in movies:
        rank += 1
        movie_info.append(
            RepeatedElement(
                {"rank": rank, "movieid": movie.movie_id, "title": movie.title}
            )
        )

    # We must have 15 movie elements for unknown reasons.
    # If a category has less than 15, repeat the last one.
    # However, for the most part, only 5 movies are shown.
    movie_info_len = len(movie_info)
    if movie_info_len != 15:
        last_movie = movie_info[movie_info_len - 1]
        repeated_movie_id = last_movie.contents.get("movieid")
        repeated_title = last_movie.contents.get("title")

        for _ in range(15 - movie_info_len):
            rank += 1
            movie_info.append(
                RepeatedElement(
                    {
                        "rank": rank,
                        "movieid": repeated_movie_id,
                        "title": repeated_title,
                    }
                )
            )

    return {"leftmovieinfo": movie_info, "rightmovieinfo": movie_info}


@app.route("/url2/evaluate.cgi", methods=["GET", "POST"])
@xml_node_name("Evaluate")
def evaluate():
    # TODO! Write mii to a database!
    return {"code": 1, "msg": "awesome thanks"}

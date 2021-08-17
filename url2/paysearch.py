from flask import request
from helpers import xml_node_name, RepeatedElement, iso_date_and_time
from models import PayMovies
from room import app

EMPTY_RESPONSE = {"num": 1, "categid": 12345}


@app.route("/url2/pay/psearch.cgi")
@xml_node_name("PaySearchMovies")
def pay_search():
    q = request.args.get("q")
    if q is None:
        return EMPTY_RESPONSE

    pay_movies = PayMovies.query.search(q).limit(64).all()

    movie_infos = []
    rank = 0
    for pay_movie in pay_movies:
        rank += 1
        movie_infos.append(
            RepeatedElement(
                {
                    "rank": rank,
                    "movieid": pay_movie.movie_id,
                    "title": pay_movie.title,
                    "kana": "12345678",
                    "refid": "01234567890123456789012345678912",
                    "strdt": iso_date_and_time(pay_movie.date_added),
                    "pop": 0,
                    "released": pay_movie.released,
                    "term": 1,
                    "price": pay_movie.price,
                }
            )
        )

    if movie_infos:
        return {"num": 1, "categid": 12345, "movieinfo": movie_infos}
    else:
        return {"num": 1, "categid": 12345}

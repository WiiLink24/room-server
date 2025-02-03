from flask import request
from werkzeug import exceptions

from models import Movies, PayMovies, EvaluateData, db
from room import app
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
        .filter(Movies.unlisted == False)
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


@app.route("/url2/pay/prelated.cgi")
@xml_node_name("PayRelatedMovies")
def pay_related():
    movie = request.args.get("movieid")
    category_result = PayMovies.query.filter_by(movie_id=movie).first()
    if category_result is None:
        return exceptions.NotFound()

    category_id = category_result.category_id

    movies = (
        PayMovies.query.filter(PayMovies.category_id == category_id)
        .filter(Movies.unlisted == False)
        .order_by(PayMovies.date_added)
        .limit(4)
        .all()
    )

    movie_info = []

    rank = 0

    for movie in movies:
        rank += 1
        movie_info.append(
            RepeatedElement(
                {
                    "rank": rank,
                    "movieid": movie.movie_id,
                    "title": movie.title,
                }
            )
        )

    movie_info_len = len(movie_info)
    if movie_info_len != 4:
        last_movie = movie_info[movie_info_len - 1]
        repeated_movie_id = last_movie.contents.get("movieid")
        repeated_title = last_movie.contents.get("title")

        for i in range(4 - movie_info_len):
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

    return {"movieinfo": movie_info}


@app.route("/url2/pay/pevaluate.cgi", methods=["GET", "POST"])
@xml_node_name("PayEvaluate")
def pay_evaluate():
    # The form returns metrics such as watch time, wii number, mac address and if the user sent to DSi.
    # We do not care about this stuff, so we will just return success
    return {"code": 1, "msg": "awesome thanks"}


@app.route("/url2/evaluate.cgi", methods=["GET", "POST"])
@xml_node_name("Evaluate")
def evaluate():
    if request.form.get("wiiid") == "0000000000000000":
        # We won't count votes made on Dolphin without a real NAND
        return {"code": 1, "msg": "awesome thanks"}

    # 8 is the maximum amount of Mii's that can be registered.
    for i in range(8):
        vote = request.form.get("eval%s" % i)
        gender = request.form.get("sex%s" % i)
        blood = request.form.get("blood%s" % i)
        age = request.form.get("age%s" % i)
        movie_id = request.form.get("movieid")
        if vote:
            data = EvaluateData(
                movie_id=movie_id, gender=gender, blood=blood, age=age, vote=vote
            )

            db.session.add(data)
            db.session.commit()
        else:
            # Either this Mii didn't vote, or doesn't exist
            continue

    return {"code": 1, "msg": "awesome thanks"}

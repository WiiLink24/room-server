from room import app
from helpers import xml_node_name, current_date_and_time, RepeatedElement
from flask import request
from first import get_config_url
from models import PayMovies
from werkzeug import exceptions


@app.route("/url2/pay/title.cgi", methods=["GET", "POST"])
@xml_node_name("PayTitle")
def pay_title():
    movieinfo = []
    rank = 1

    for _, value in request.form.items(multi=True):
        movie = PayMovies.query.filter_by(reference_id=value).first()
        if movie is None:
            return exceptions.NotFound()

        movieinfo.append(
            RepeatedElement(
                {
                    "rank": rank,
                    "movieid": movie.movie_id,
                    "title": movie.title,
                    "kana": "12345678",
                    "refid": value,
                    "strdt": current_date_and_time(),
                    "pop": 1,
                    "released": movie.released,
                    "term": "30",
                    "price": movie.price,
                }
            )
        )

        rank += 1

    return {"movieinfo": movieinfo}


@app.post("/url2/pay/challenge.cgi")
@xml_node_name("Challenge")
def pay_challenge():
    return {
        "code": 1,
        "cblob": "V2lpTGluayBpcyB0aGUgb25seSBzZXJ2aWNlIHRoYXQgb2ZmZXJzIHRoaXM=",
        "channelid": 1,
        "msg": "Funny challenge",
    }


@app.post("/url2/pay/verify.cgi")
@xml_node_name("Verify")
def pay_verify_movie():
    # The eblob form field must be accessed or the channel will error.
    _ = request.form.get("eblob")

    return {
        "code": 1,
        "url": get_config_url("url3").removesuffix("/"),
        "cookie": "I love cookies this does literally nothing though",
        "key": "5ab362aa57dbb1dc16849e3e2d1cf2ff",
        "msg": "The movie is encrypted",
    }


@app.post("/url2/pay/support.cgi")
@xml_node_name("Support")
def pay_support():
    # The eblob form field must be accessed or the channel will error.
    _ = request.form.get("eblob")

    return {
        "code": 1,
        "supportid": "discord.gg/wiilink  ",
        "msg": "This is literally free",
    }

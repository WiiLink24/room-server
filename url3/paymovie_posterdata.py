from flask import send_from_directory
from werkzeug import exceptions
from werkzeug.security import safe_join

from room import app, db
from helpers import RepeatedElement, xml_node_name, current_date_and_time
from models import PayMovies


@app.route("/url3/pay/list/category/search/<category_id>")
# Grabs the Poster Data
@xml_node_name("SearchMovies")
def search_movies(category_id):
    retrieved_data = (
        db.session.query(PayMovies)
        .filter(PayMovies.category_id == category_id)
        .order_by(PayMovies.movie_id)
        .all()
    )
    results = []

    if not retrieved_data:
        # Looks like this category does not exist, or contains no movies.
        return exceptions.NotFound()

    for i, paycategoryposters in enumerate(retrieved_data):
        results.append(
            RepeatedElement(
                {
                    "rank": i + 1,
                    "movieid": paycategoryposters.movie_id,
                    "title": paycategoryposters.title,
                    "strdt": current_date_and_time(),
                    "pop": "1",
                    "kana": 12345678,
                    "refid": "01234567890123456789012345678912",
                    "released": paycategoryposters.released,
                    "term": 1,
                    "price": paycategoryposters.price,
                }
            )
        )

    return {
        "num": "1",
        "categid": category_id,
        "movieinfo": results,
    }


if app.debug:

    @app.route("/url3/pay/movie/<unk>/<name>/<name1>.img")
    # Grabs the Poster
    def serve_pay_movie_poster(unk, name, name1):
        return send_from_directory(
            safe_join("assets/pay-movie/", unk, name), name1 + ".img"
        )

    @app.route("/url3/pay/movie/<unk>/name>/<name1>.img")
    # Grabs the smaller picture you will see when you click the poster
    def serve_pay_images_payment(unk, name, name1):
        return send_from_directory(
            safe_join("assets/pay-movie/", unk, name), name1 + ".img"
        )

    @app.route("/url3/pay/movie/<unk>/<name>/<name1>.smo")
    # Grabs the trailer
    def serve_pay_trailer(unk, name, name1):
        return send_from_directory(
            safe_join("assets/pay-movie/", unk, name), name1 + ".smo"
        )

    @app.route("/url3/pay/movie/<unk>/<name>/<name1>.sem")
    # Grabs the encrypted trailer
    def serve_pay_enc_trailer(unk, name, name1):
        return send_from_directory(
            safe_join("assets/pay-movie/", unk, name), name1 + ".sem"
        )

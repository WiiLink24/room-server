from flask import send_from_directory
from werkzeug import exceptions
from werkzeug.security import safe_join

from room import app
from helpers import RepeatedElement, xml_node_name, current_date_and_time
from models import PayMovies, db


@app.route("/url3/pay/list/category/search/<category_id>")
@xml_node_name("SearchMovies")
def search_movies(category_id):
    retrieved_data = (
        db.session.query(PayMovies)
        .filter(PayMovies.category_id == category_id)
        .order_by(PayMovies.movie_id)
        .all()
    )
    if not retrieved_data:
        # Looks like this category does not exist, or contains no movies.
        return exceptions.NotFound()

    results = [
        RepeatedElement(
            {
                "rank": i + 1,
                "movieid": paycategoryposters.movie_id,
                "title": paycategoryposters.title,
                "strdt": current_date_and_time(),
                "pop": "1",
                "kana": 12345678,
                "refid": paycategoryposters.reference_id,
                "released": paycategoryposters.released,
                "term": 30,
                "price": paycategoryposters.price,
            }
        )
        for i, paycategoryposters in enumerate(retrieved_data)
    ]
    return {
        "num": "1",
        "categid": category_id,
        "movieinfo": results,
    }


if app.debug:

    @app.route("/url3/pay/movie/<unk>/<name>/<name1>.img")
    def serve_pay_movie_poster(unk, name, name1):
        return send_from_directory(
            safe_join("assets/pay-movie/", unk, name), f"{name1}.img"
        )

    @app.route("/url3/pay/movie/<unk>/name>/<name1>.img")
    def serve_pay_images_payment(unk, name, name1):
        return send_from_directory(
            safe_join("assets/pay-movie/", unk, name), f"{name1}.img"
        )

    @app.route("/url3/pay/movie/<unk>/<name>/<name1>.smo")
    def serve_pay_trailer(unk, name, name1):
        return send_from_directory(
            safe_join("assets/pay-movie/", unk, name), f"{name1}.smo"
        )

    @app.route("/url3/pay/movie/<unk>/<name>/<name1>.emo")
    def serve_pay_movie(unk, name, name1):
        return send_from_directory(
            safe_join("assets/pay-movie/", unk, name), f"{name1}.emo"
        )

    @app.route("/url3/pay/movie/<unk>/<name>/<name1>.sem")
    def serve_pay_enc_trailer(unk, name, name1):
        return send_from_directory(
            safe_join("assets/pay-movie/", unk, name), f"{name1}.sem"
        )

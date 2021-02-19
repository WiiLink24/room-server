from flask import send_from_directory, safe_join
from werkzeug import exceptions

from room import app, db
from helpers import RepeatedElement, xml_node_name, current_date_and_time
from models import PayCategoriesPosters


@app.route("/url3/pay/list/category/search/<category_id>")
# Grabs the Poster Data
@xml_node_name("SearchMovies")
def search_movies(category_id):
    retrieved_data = (
        db.session.query(PayCategoriesPosters)
        .filter(PayCategoriesPosters.category_id == category_id)
        .order_by(PayCategoriesPosters.movieid)
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
                    "rank": paycategoryposters.rank,
                    "movieid": paycategoryposters.movieid,
                    "title": paycategoryposters.title,
                    "strdt": current_date_and_time(),
                    "pop": paycategoryposters.pop,
                    "kana": 12345678,
                    "refid": "01234567890123456789012345678912",
                    "released": paycategoryposters.release_date,
                    "term": 1,
                    "price": paycategoryposters.price,
                }
            )
        )

    return {
        "num": paycategoryposters.num,
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

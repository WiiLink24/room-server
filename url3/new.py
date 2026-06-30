from room import app
from helpers import xml_node_name, RepeatedElement, current_date_and_time, wii_locale
from models import PayMovies, db, PayCategories


@app.route("/url3/pay/list/new/all.xml")
@xml_node_name("New")
def pay_new_all():
    queried_movies = (
        db.session.query(PayMovies, PayCategories)
        .filter(PayMovies.category_id == PayCategories.category_id)
        .where(PayCategories.locale == wii_locale)
        .order_by(PayMovies.date_added.desc())
        .limit(64)
    )
    filler = []

    for i, new_movies in enumerate(queried_movies):
        # Items must be indexed by 1.
        filler.append(
            RepeatedElement(
                {
                    "rank": i + 1,
                    "movieid": new_movies.movie_id,
                    "title": new_movies.title,
                    "strdt": current_date_and_time(),
                    "pop": "1",
                    "kana": 12345678,
                    "refid": "01234567890123456789012345678912",
                    "released": new_movies.released,
                    "term": 1,
                    "price": new_movies.price,
                }
            )
        )

    return {
        "movieinfo": filler,
    }

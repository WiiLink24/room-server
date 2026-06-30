from room import app
from helpers import xml_node_name, RepeatedElement, current_date_and_time, wii_locale
from models import Movies, Categories, db


@app.route("/url1/list/new/all.xml")
@xml_node_name("New")
def new_all():
    queried_movies = (
        db.session.query(Movies, Categories)
        .filter(Movies.category_id == Categories.category_id)
        .where(Categories.locale == wii_locale)
        .with_entities(Movies.title, Movies.movie_id)
        .order_by(Movies.date_added.desc())
        .limit(12)
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
                    "genre": 1,
                    "strdt": current_date_and_time(),
                    "pop": 0,
                }
            )
        )

    return {
        "movieinfo": filler,
    }

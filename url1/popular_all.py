from sqlalchemy import func

from models import EvaluateData, Movies
from room import app, db
from helpers import xml_node_name, RepeatedElement, current_date_and_time


@app.route("/url1/list/popular/all.xml")
@xml_node_name("Popular")
def popular_all():
    # Sort for the all time popular movies.
    popular_movies = (
        db.session.query(EvaluateData, Movies)
        # Select movie_id and title...
        .with_entities(EvaluateData.movie_id, Movies.title)
        # ...by grouping together all duplicate movie votes to their title...
        .group_by(EvaluateData.movie_id, Movies.title)
        # ...then join together the movie_id of EvaluateData to that of Movies for title...
        .filter(EvaluateData.movie_id == Movies.movie_id)
        # ...and then sort by highest voted movies...
        .order_by(func.sum(EvaluateData.vote).desc())
        # ...but no more than 64 of them.
        .limit(64).all()
    )

    movieinfo = []
    for i, movie in enumerate(popular_movies):
        # Items must be indexed by 1.
        movieinfo.append(
            RepeatedElement(
                {
                    "rank": i + 1,
                    "movieid": movie.movie_id,
                    "title": movie.title,
                    "genre": 1,
                    "strdt": current_date_and_time(),
                    "pop": 0,
                }
            )
        )

    return {
        "movieinfo": movieinfo,
    }

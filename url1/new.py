from room import app
from helpers import xml_node_name, RepeatedElement, current_date_and_time
from models import Movies


@app.route("/url1/list/new/all.xml")
@xml_node_name("New")
def new_all():
    queried_movies = Movies.query.order_by(Movies.date_added.desc()).limit(12)
    filler = [
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
        for i, new_movies in enumerate(queried_movies)
    ]
    return {
        "movieinfo": filler,
    }

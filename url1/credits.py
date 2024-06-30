from room import app
from helpers import xml_node_name, RepeatedElement
from models import MovieCredits
from werkzeug import exceptions


@app.route("/url1/movie/<md5>/<int:movie_id>.stf")
@xml_node_name("MovieStaff")
def _credits(md5, movie_id):
    queried_credits = (
        MovieCredits.query.filter_by(movie_id=movie_id)
        .order_by(MovieCredits.order.asc())
        .all()
    )
    if queried_credits is None:
        return exceptions.NotFound()

    results = []
    for c in queried_credits:
        results.append(
            RepeatedElement({"seq": c.order, "role": c.role, "name": c.name})
        )

    return {"staff": results}

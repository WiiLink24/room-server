from flask import send_from_directory
from werkzeug import exceptions

from room import app
from helpers import xml_node_name, is_v770
from models import Posters


@app.route("/url1/wall/<int:met_id>.met")
@xml_node_name("PosterMeta")
def wall_metadata(met_id: int):
    if is_v770:
        # v770 requires we have poster metadata for the poster in the back of the room.
        if met_id == 2:
            return {
                "posterid": 2,
                "msg": "Hi, v770!",
                "movieid": 2,
                "title": "Welcome to Wii Room!",
            }

        # Additionally, we hardcode anything above 100000 to be the same as normal.
        # We split the metadata from its imagery due to a need for different dimensions.
        if met_id > 1000000 and is_v770:
            met_id -= 1000000

    # Determine if we have metadata for this poster.
    poster_metadata = Posters.query.filter_by(poster_id=met_id).first()
    if poster_metadata is None:
        return exceptions.NotFound()

    return {
        "posterid": poster_metadata.poster_id,
        "msg": poster_metadata.msg,
        "movieid": poster_metadata.movie_id,
        "title": poster_metadata.title,
    }


if app.debug:

    @app.route("/url1/wall/<name>.img")
    def serve_images(name):
        return send_from_directory("assets/normal-wall", name + ".img")

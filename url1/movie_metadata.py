from flask import send_from_directory, safe_join
from werkzeug import exceptions

from room import app
from helpers import xml_node_name
from models import Movies


@app.route("/url1/movie/<unk>/<int:movie_id>.met")
@xml_node_name("MovieMeta")
def movie_metadata(unk, movie_id: int):
    # Determine if we have metadata for this poster.
    metadata = Movies.query.filter_by(movie_id=movie_id).first()
    if metadata is None:
        return exceptions.NotFound()

    # Wii no Ma expects the response to be ordered as follows.
    movie = {
        "movieid": metadata.movie_id,
        "title": metadata.title,
        "len": metadata.length,
        "aspect": metadata.aspect,
        "genre": metadata.genre,
        "sppageid": metadata.sp_page_id,
        "dsdist": metadata.ds_dist,
    }

    # This key must follow "dsdist" if used.
    if metadata.ds_dist:
        movie["dsmovid"] = metadata.ds_mov_id

    # Staff must be the final key.
    movie["staff"] = metadata.staff
    return movie


if app.debug:

    @app.route("/url1/movie/<unk>/<name>.img")
    def serve_movie_poster(unk, name):
        return send_from_directory(safe_join("assets/movies/", unk), name + ".img")

    @app.route("/url1/movie/<unk>/<name>.mov")
    def serve_movie_mov(unk, name):
        return send_from_directory(safe_join("assets/movies/", unk), name + ".mov")

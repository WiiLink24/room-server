from flask import send_from_directory
from werkzeug import exceptions
from werkzeug.security import safe_join

from room import app
from helpers import xml_node_name
from models import Movies


@app.route("/url1/movie/<_hash_byte>/<int:movie_id>.met")
@xml_node_name("MovieMeta")
def movie_metadata(_hash_byte, movie_id: int):
    # Determine if we have metadata for this poster.
    metadata = Movies.query.filter_by(movie_id=movie_id).first()
    if metadata is None:
        return exceptions.NotFound()

    # If a ds_mov_id is present for this row, present it.
    has_ds_mov = metadata.ds_mov_id is not None

    movie = {
        "movieid": metadata.movie_id,
        "title": metadata.title,
        "len": metadata.length,
        "aspect": metadata.aspect,
        "genre": metadata.genre,
        "sppageid": metadata.sp_page_id,
        "dsdist": has_ds_mov,
    }

    # This key must follow "dsdist" if used.
    if has_ds_mov:
        movie["dsmovid"] = metadata.ds_mov_id

    # Staff must be the final key.
    movie["staff"] = metadata.staff
    return movie


if app.debug:

    @app.route("/url1/movie/<unk>/<name>.img")
    def serve_movie_poster(unk, name):
        return send_from_directory(safe_join("assets/movies/", unk), f"{name}.img")

    @app.route("/url1/movie/<unk>/<name>.mov")
    def serve_movie_mov(unk, name):
        return send_from_directory(safe_join("assets/movies/", unk), f"{name}.mov")

    @app.route("/url1/dsmov/<unk>/<name>.enc")
    def serve_dsmov(unk, name):
        return send_from_directory(safe_join("assets/dsmov/", unk), f"{name}.mov")

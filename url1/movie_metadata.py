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

    return {
        "movieid": metadata.movie_id,
        "title": metadata.title,
        "len": metadata.length,
        "aspect": metadata.aspect,
        "genre": metadata.genre,
        "sppageid": metadata.sp_page_id,
        "dsdist": metadata.ds_dist,
        "staff": metadata.staff,
    }

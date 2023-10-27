from flask import send_from_directory
from werkzeug import exceptions

from room import app
from helpers import xml_node_name
from models import PayPosters


@app.route("/url3/pay/wall/<int:met_id>.met")
@xml_node_name("PosterMeta")
def pay_wall_metadata(met_id: int):
    # Determine if we have metadata for this poster.
    poster_metadata = PayPosters.query.filter_by(poster_id=met_id).first()
    if poster_metadata is None:
        return exceptions.NotFound()

    return {
        "posterid": poster_metadata.poster_id,
        "msg": poster_metadata.msg,
        "movieid": poster_metadata.poster_id,
        "title": poster_metadata.title,
        "type": poster_metadata.type,
        "aspect": poster_metadata.aspect,
    }


if app.debug:

    @app.route("/url3/pay/wall/<name>.img")
    def serve_pay_images(name):
        return send_from_directory("assets/pay-wall", f"{name}.img")

    @app.route("/url3/pay/wall/<name>-H.emo")
    @app.route("/url3/pay/wall/<name>-L.emo")
    def serve_pay_poster_trailers(name):
        return send_from_directory("assets/pay-wall", f"{name}.emo")

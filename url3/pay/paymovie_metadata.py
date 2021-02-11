from flask import send_from_directory, safe_join
from werkzeug import exceptions

from room import app
from helpers import xml_node_name
from models import PayMovies

if app.debug:

    @app.route("/url3/pay/movie/<unk>/<int:num>/<int:num1>.met")
    @xml_node_name("PayMovies")
    def pay_category_metadata(unk, num, num1: int):
        # Determine if we have metadata for this poster.
        payposter_metadata = PayMovies.query.filter_by(movie_id=num1).first()
        if payposter_metadata is None:
            return exceptions.NotFound()

        return {
            "movieid": payposter_metadata.movie_id,
            "title": payposter_metadata.title,
            "kana": "12345678",
            "len": payposter_metadata.length,
            "aspect": payposter_metadata.aspect,
            "payenddt": payposter_metadata.payenddt,
            "dsdist": payposter_metadata.ds_dist,
            "dsmovid": payposter_metadata.ds_mov_id,
            "staff": payposter_metadata.staff,
            "note": payposter_metadata.note,
            "dimg": payposter_metadata.dimg,
            "eval": payposter_metadata.eval,
            "refid": "01234567890123456789012345678912",
            "pricecd": "1234567",
            "term": "30",
            "price": payposter_metadata.price,
            "sample": payposter_metadata.sample,
            "smpap": payposter_metadata.smpap,
            "released": payposter_metadata.released,
            "encrypt": "0",
            "geofilter": "1",
        }

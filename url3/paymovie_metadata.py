from werkzeug import exceptions

from room import app
from helpers import xml_node_name
from models import PayMovies


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
        "aspect": 1,
        "payenddt": "2022-12-12T23:00:00",
        "dsdist": 1,
        "dsmovid": payposter_metadata.movie_id,
        "staff": 1,
        "note": payposter_metadata.note,
        "dimg": 1,
        "eval": 0,
        "refid": "01234567890123456789012345678912",
        "pricecd": "1234567",
        "term": "30",
        "price": payposter_metadata.price,
        "sample": 1,
        "smpap": 1,
        "released": payposter_metadata.released,
        "encrypt": "0",
        "geofilter": "1",
    }

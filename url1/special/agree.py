from room import app
from helpers import xml_node_name


@app.route("/url1/delivery/<movie_id>.xml")
@xml_node_name("DeliveryAgree")
def delivery_agree(movie_id):
    return {
        "agree": "Agree to terms and conditions"
    }


@app.route("/url1/coupon/<movie_id>.xml")
@xml_node_name("DeliveryAgree")
def coupon_agree(movie_id):
    return {
        "agree": "Get Wii Room GO ready!"
    }

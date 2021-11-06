from helpers import xml_node_name
from room import app, db


@app.route("/url2/pay/rivtoken.cgi", methods=["GET", "POST"])
@xml_node_name("RIVToken")
def riv_token():
    return {"code": 1,
            "token": 1,
            "msg": "Vote recorded."
    }

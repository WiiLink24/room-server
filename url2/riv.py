from helpers import xml_node_name
from flask import send_from_directory
from room import app


@app.route("/url2/pay/rivtoken.cgi", methods=["GET", "POST"])
@xml_node_name("RIVToken")
def riv_token():
    return {"code": 1, "token": 1, "msg": "Vote recorded."}


@app.post("/test")
def test():
    return send_from_directory("./assets/delivery", "1.xml")

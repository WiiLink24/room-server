from room import app
from helpers import xml_node_name


@app.route("/url2/smp.cgi", methods=["POST"])
@xml_node_name("Delivery")
def delivery_response():
    """This is 100% not apart of url2 however I don't know where else to put this"""
    return {"code": 1, "msg": "Vote recorded."}

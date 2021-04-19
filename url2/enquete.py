from helpers import xml_node_name
from room import app


@app.route("/url2/enquete.cgi")
@xml_node_name("Enquete")
def handle_enquete():
    return {"code": "2", "msg": "Vote recorded."}

from room import app
from helpers import xml_node_name


@app.route("/url1/beacon/<unused_id>")
@xml_node_name("SampleRequest")
def beacon(unused_id):
    # This route is most likely used for analytics.
    # We do not need, nor desire analytics.
    # Additionally, that is most likely the incorrect node name.
    # Wii no Ma seems to only care if ver exists.

    return {"code": "1", "msg": "hi"}

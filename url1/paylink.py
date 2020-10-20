from room import app
from helpers import xml_node_name


@app.route("/url1/conf2/paylink.xml")
@xml_node_name("MovieLink")
def conf_paylink():
    return {
        "linkinfo": {
            "movieid": "2",
            "categid": "11111",
        }
    }

from room import app
from helpers import xml_node_name, is_v770


@app.route("/url1/conf2/paylink.xml")
@xml_node_name("MovieLink")
def conf_paylink():
    if is_v770():
        return conf_paylink_v770()
    else:
        return conf_paylink_v1025()


def conf_paylink_v1025():
    return {
        "linkinfo": {
            "movieid": "2",
            "categid": "11111",
        }
    }


def conf_paylink_v770():
    return {
        "linkinfo": {
            "movieid": "1",
            "paymovid": "1",
        }
    }

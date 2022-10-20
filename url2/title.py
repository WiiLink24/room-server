from room import app
from helpers import xml_node_name, current_date_and_time


@app.route("/url2/pay/title.cgi", methods=["GET", "POST"])
@xml_node_name("PayTitle")
def pay_title():
    return {
        "movieinfo": {
            "rank": 1,
            "movieid": 1,
            "title": "Captain America: Civil War",
            "kana": "12345678",
            "refid": "01234567890123456789012345678912",
            "strdt": current_date_and_time(),
            "pop": 1,
            "released": "2016-04-21",
            "term": "30",
            "price": 0
        }
    }

from room import app
from helpers import (
    current_date_and_time,
    xml_node_name,
    parse_caldate,
    get_weekday,
    iso_date,
)


@app.route("/url1/caldaily/<date>.xml")
@xml_node_name("CalDaily")
def cal_daily(date):
    current_date = parse_caldate(date)

    return {
        "date": iso_date(current_date),
        "wday": get_weekday(current_date),
        "holiday": 1,
        "movieinfo": {
            "seq": 1,
            "movieid": 1,
            "strdt": current_date_and_time(),
            "enddt": current_date_and_time(),
            "title": "Sketch is Dead",
        },
        "trivia": {
            "tindex": 1,
            "thead": "Howdy",
            "tdetail": "There are flying foxes.",
            "timg": 1,
            "timgnum": 1,
            "tbgm": 1,
        },
    }

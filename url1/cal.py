import datetime

from room import app
from helpers import (
    xml_node_name,
    parse_caldate,
    get_weekday,
    iso_date,
    current_date_and_time,
    RepeatedElement,
)


@app.route("/url1/cal/<date>.xml")
@xml_node_name("Calendar")
def cal(date):
    passed_date = parse_caldate(date)
    response_dict = []

    # We must gather data for every day in a week.
    # Range 0 to 6 so we have 7 numbers with one being the current day.
    for day_num in range(7):
        current_date = passed_date + datetime.timedelta(days=day_num)

        date_info = {
            "date": iso_date(current_date),
            "wday": get_weekday(current_date),
            "holiday": 0,
            "thead": 0,
            "movieinfo": {
                "seq": 1,
                "movieid": 1,
                "strdt": current_date_and_time(),
                "enddt": current_date_and_time(),
                "title": "Flight of a Shiba",
            },
        }

        response_dict.append(RepeatedElement(date_info))

    return {"dateinfo": response_dict}

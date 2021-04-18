from flask import request
from helpers import xml_node_name, RepeatedElement, current_date_and_time
from room import app, es


@app.route("/url2/pay/psearch.cgi")
@xml_node_name("PaySearchMovies")
def paysearch():
    q = request.args.get("q")
    if q is None:
        return {"num": 1, "categid": 12345}

    s = es.search(index="pay_index", body={"query": {"match": {"title": q}}})
    shows = s["hits"]["hits"]

    show_ids = {}
    for i in shows:
        show_ids[i["_source"]["movie_id"]] = i["_source"]["title"]

    movieinfos = []
    rank = 0
    has_results = False
    if len(shows) != 0:
        has_results = True
        for i in show_ids.keys():
            rank += 1
            movieinfos.append(
                RepeatedElement(
                    {
                        "rank": rank,
                        "movieid": i,
                        "title": show_ids[i],
                        "kana": "12345678",
                        "refid": "01234567890123456789012345678912",
                        "strdt": current_date_and_time(),
                        "pop": 0,
                        "released": "2020-08-08",
                        "term": 1,
                        "price": "0",
                    }
                )
            )
    if has_results:
        return {"num": 1, "categid": 12345, "movieinfo": movieinfos}
    else:
        return {"num": 1, "categid": 12345}

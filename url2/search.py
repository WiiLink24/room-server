from flask import request
from helpers import xml_node_name, RepeatedElement
from room import app, es
from url2.reginfo import getzone


@app.route("/url2/search.cgi")
@xml_node_name("SearchMovies")
def search():
    q = request.args.get("q")
    if q is None:
        return {"num": 1, "categid": 12345}

    s = es.search(index="tv_index", body={"query": {"match": {"title": q}}})
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
                        "genre": 1,
                        "strdt": getzone(),
                        "pop": 0,
                    }
                )
            )
    if has_results:
        return {"num": 1, "categid": 12345, "movieinfo": movieinfos}
    else:
        return {"num": 1, "categid": 12345}

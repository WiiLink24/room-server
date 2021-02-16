from room import app
from helpers import xml_node_name, RepeatedElement


@app.route("/url2/miiinfo.cgi", methods=["GET", "POST"])
@xml_node_name("MiiInfo")
def miiinfo():
    return {"code": 0, "msg": "thanks"}


@app.route("/url2/related.cgi")
@xml_node_name("RelatedMovies")
def related():
    # Hardcoded for now
    movie_info = []
    for num in range(15):
        movie_info.append(
            RepeatedElement(
                {"rank": num + 1, "movieid": 2, "title": "Flight of a Shiba"}
            )
        )

    return {"leftmovieinfo": movie_info, "rightmovieinfo": movie_info}


@app.route("/url2/evaluate.cgi", methods=["GET", "POST"])
@xml_node_name("Evaluate")
def evaluate():
    # TODO! Write mii to a database!
    return {"code": 1, "msg": "awesome thanks"}

from helpers import xml_node_name
from room import app


@app.route("/url2/piceval.cgi", methods=["GET", "POST"])
@xml_node_name("PicEval")
def pic_eval():
    # TODO: Maybe append the data to a table. My issue (Sketch) is that I see no use for this. Nintendo most likely
    # TODO: used this for advertising data
    return {"code": 1, "msg": "Vote recorded."}

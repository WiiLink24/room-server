from helpers import xml_node_name
from room import app, db
from models import PollData
from flask import request


@app.route("/url2/enquete.cgi", methods=["GET", "POST"])
@xml_node_name("Enquete")
def handle_enquete():
    if request.form.get("macadr"[:6]) == "0017ab" or "0009bf":
        # We won't count votes made on Dolphin
        return {"code": "2", "msg": "Vote recorded."}

    for i in range(8):
        poll_id = request.form.get("enqid")
        wii_num = request.form.get("wiiid")
        choice = request.form.get("choice%s" % i)
        age = request.form.get("age%s" % i)
        gender = request.form.get("sex%s" % i)

        if choice:
            data = PollData(
                poll_id=poll_id, wii_num=wii_num, choice=choice, age=age, gender=gender
            )
            db.session.add(data)
            db.session.commit()
        else:
            # Either this Mii didn't vote, or doesn't exist
            continue

    return {"code": "2", "msg": "Vote recorded."}

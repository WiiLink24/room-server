from helpers import xml_node_name
from room import app
from models import PollData, db
from flask import request


@app.route("/url2/enquete.cgi", methods=["GET", "POST"])
@xml_node_name("Enquete")
def handle_enquete():
    if request.form.get("wiiid") == "0000000000000000":
        # We won't count votes made on Dolphin without a real NAND
        return {"code": "2", "msg": "Vote recorded."}

    for i in range(8):
        poll_id = request.form.get("enqid")
        wii_num = request.form.get("wiiid")
        choice = request.form.get(f"choice{i}")
        age = request.form.get(f"age{i}")
        gender = request.form.get(f"sex{i}")

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

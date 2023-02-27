from room import app, db
from flask import request
from helpers import xml_node_name
from models import Giveaways


@app.route("/url2/smp.cgi", methods=["POST"])
@xml_node_name("Delivery")
def delivery_response():
    wii_id = request.form.get("wiiid")
    giveaway_id = request.form.get("smpid")
    email = request.form.get("mail")

    user = Giveaways.query.filter_by(giveaway_id=giveaway_id).filter_by(wii_id=wii_id).first()
    if user is None:
        data = Giveaways(giveaway_id=giveaway_id, wii_id=wii_id, email=email)
        db.session.add(data)
        db.session.commit()

    return {"code": 1, "msg": "Vote recorded."}

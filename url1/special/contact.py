from helpers import xml_node_name
from werkzeug import exceptions
from room import app
from models import Rooms


@app.route("/url1/special/<int:page_id>/contact.xml")
@xml_node_name("SpContact")
def special_contact_n(page_id: int):
    retrieved_data = Rooms.query.filter_by(room_id=page_id).first()
    if retrieved_data is None or retrieved_data.contact_data is None:
        return exceptions.NotFound()

    return {"contact": retrieved_data.contact_data}

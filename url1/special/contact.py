from helpers import xml_node_name
from werkzeug import exceptions
from room import app
from models import Rooms


@app.route("/url1/special/<int:_page>/contact.xml")
@xml_node_name("SpContact")
def special_contact_n(_page: int):
    retrieved_data = Rooms.query.filter_by(room_id=_page).first()
    if retrieved_data is None:
        return exceptions.NotFound()

    return {
        "contact": retrieved_data.contact_data
    }

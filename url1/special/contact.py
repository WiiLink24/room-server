from helpers import xml_node_name
from room import app


@app.route("/url1/special/<_page>/contact.xml")
@xml_node_name("SpContact")
def special_contact_n(_page):
    return {"contact": "Join us on Discord at https://discord.gg/n4ta3w6!"}

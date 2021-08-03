from models import EvaluateData
from room import app
from helpers import xml_node_name
from url1.popular_all import query_popular


@app.route("/url1/list/popular/11.xml")
@xml_node_name("Popular")
def popular_blood_a():
    return {
        "type": 1,
        "movieinfo": query_popular(EvaluateData.blood == 1),
    }


@app.route("/url1/list/popular/12.xml")
@xml_node_name("Popular")
def popular_blood_b():
    return {
        "type": 1,
        "movieinfo": query_popular(EvaluateData.blood == 2),
    }


@app.route("/url1/list/popular/13.xml")
@xml_node_name("Popular")
def popular_blood_o():
    return {
        "type": 1,
        "movieinfo": query_popular(EvaluateData.blood == 3),
    }


@app.route("/url1/list/popular/14.xml")
@xml_node_name("Popular")
def popular_blood_ab():
    return {
        "type": 1,
        "movieinfo": query_popular(EvaluateData.blood == 4),
    }

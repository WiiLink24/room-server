from models import EvaluateData
from room import app
from helpers import xml_node_name
from url1.popular_all import query_popular


@app.route("/url1/list/popular/01.xml")
@xml_node_name("Popular")
def popular_male():
    return {
        "type": 1,
        "movieinfo": query_popular(EvaluateData.gender == 1),
    }


@app.route("/url1/list/popular/02.xml")
@xml_node_name("Popular")
def popular_female():
    return {
        "type": 1,
        "movieinfo": query_popular(EvaluateData.gender == 2),
    }


@app.route("/url1/list/popular/03.xml")
@xml_node_name("Popular")
def popular_under_age_9():
    return {
        "type": 1,
        "movieinfo": query_popular(EvaluateData.age < 9),
    }


@app.route("/url1/list/popular/04.xml")
@xml_node_name("Popular")
def popular_age_10():
    return {
        "type": 1,
        "movieinfo": query_popular(EvaluateData.age >= 10, EvaluateData.age < 20),
    }


@app.route("/url1/list/popular/05.xml")
@xml_node_name("Popular")
def popular_age_20():
    return {
        "type": 1,
        "movieinfo": query_popular(EvaluateData.age >= 20, EvaluateData.age < 30),
    }


@app.route("/url1/list/popular/06.xml")
@xml_node_name("Popular")
def popular_age_30():
    return {
        "type": 1,
        "movieinfo": query_popular(EvaluateData.age >= 30, EvaluateData.age < 40),
    }


@app.route("/url1/list/popular/07.xml")
@xml_node_name("Popular")
def popular_age_40():
    return {
        "type": 1,
        "movieinfo": query_popular(EvaluateData.age >= 40, EvaluateData.age < 50),
    }


@app.route("/url1/list/popular/08.xml")
@xml_node_name("Popular")
def popular_age_50():
    return {
        "type": 1,
        "movieinfo": query_popular(EvaluateData.age >= 50, EvaluateData.age < 60),
    }


@app.route("/url1/list/popular/09.xml")
@xml_node_name("Popular")
def popular_age_60():
    return {
        "type": 1,
        "movieinfo": query_popular(EvaluateData.age >= 60, EvaluateData.age < 70),
    }


@app.route("/url1/list/popular/10.xml")
@xml_node_name("Popular")
def popular_age_over_70():
    return {
        "type": 1,
        "movieinfo": query_popular(EvaluateData.age >= 70),
    }

"""
Since there a 6 different types of Room Types, it makes no sense to make a table for each.
Instead, we use the raw JSON format of the types then convert them to xml when it is passed
through the page.py script. All of the types are in their own functions, which will be used
in The Underground when appending a new type to the database.
"""


def smp(id, title):
    return {
        "type": 1,
        "imageid": "a1234",
        "smp": {
            "smpid": id,
            "smptitle": title,
            "smpurl": "http://old.wiilink24.com",
            "smpmov": 1,
            "smpmovap": 1,
            "smpdup": 1,
        },
    }


def enq():
    return {"Still working on it"}


def mov(movie_id, title):
    return {"type": 3, "imageid": "c1234", "mov": {"movieid": movie_id, "title": title}}


def coupon(id, title):
    return {
        "type": 4,
        "imageid": "d1234",
        "coup": {
            "coupid": id,
            "couptitle": title,
            "couplimit": 10,
            "coupmov": 1,
            "coupmovap": 0,
        },
    }


def link(id, title, bgm):
    return {
        "type": 5,
        "imageid": "h1234",
        "link": {
            "linkid": id,
            "linktitle": title,
            "linktype": 1,
            "linkmov": 1,
            "linkmovap": 1,
            "linkpicnum": 1,
            "linkurl": "http://old.wiilink24.com",
            "linkpicbgm": bgm,
        },
    }


def pic(id, title, bgm):
    return {
        "type": 6,
        "imageid": "i1234",
        "pic": {
            "picid": id,
            "pictitle": title,
            "picmov": 1,
            "picmovap": 1,
            "picnum": 1,
            "picbgm": bgm,
        },
    }

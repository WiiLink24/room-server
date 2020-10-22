from flask import send_from_directory
from room import app


@app.route("/conf/first.bin")
def conf_first_bin():
    return send_from_directory("conf", "first.bin")


@app.route("/url1/wall/<name>.img")
def serve_images(name):
    return send_from_directory("assets/normal-wall", name + ".img")


@app.route("/url3/pay/wall/<name>.img")
def serve_pay_images(name):
    return send_from_directory("assets/pay-wall", name + ".img")


@app.route("/url1/intro/<name>.img")
def serve_intro(name):
    return send_from_directory("assets/normal-intro", name + ".img")


@app.route("/url3/pay/intro/<name>.img")
def serve_pay_intro(name):
    return send_from_directory("assets/pay-intro", name + ".img")


@app.route("/url1/list/category/img/<name>.img")
def serve_category_images(name):
    return send_from_directory("assets/normal-category", name + ".img")


@app.route("/url3/pay/list/category/img/<name>.img")
def serve_pay_category_images(name):
    return send_from_directory("assets/pay-category", name + ".img")


@app.route("/url1/movie/<unk>/<name>.img")
def serve_movie_poster(unk, name):
    return send_from_directory("assets/movies", name + ".img")


@app.route("/url1/movie/<unk>/<name>.mov")
def serve_movie_mov(unk, name):
    return send_from_directory("assets/movies", name + ".mov")

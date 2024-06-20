import uuid

from flask import url_for, flash, render_template, send_from_directory
from werkzeug.utils import redirect
from flask_oidc import OpenIDConnect
from models import User, db
from room import app

oidc = OpenIDConnect(app)

@app.context_processor
def inject_oidc():
    return dict(oidc=oidc)

@app.login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("root"))

@app.route("/")
def index():
    return redirect(url_for("root"))


@app.route("/theunderground")
@app.route("/theunderground/")
def root():
    return redirect(url_for("login"))


@app.route("/theunderground/login")
def login():
    if oidc.user_loggedin:
        return redirect(url_for("admin"))
    
    return render_template('login.html')


@app.route("/theunderground/logout")
@oidc.require_login
def logout():
    oidc.logout()
    response = redirect(url_for("loggedout"))
    response.set_cookie("session", expires=0)
    return response

@app.route("/theunderground/loggedout")
def loggedout():
    return render_template('loggedout.html')

@app.route("/theunderground/admin")
@oidc.require_login
def admin():
    return render_template("underground.html")

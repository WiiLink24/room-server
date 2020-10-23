from config import underground_enabled
from flask import render_template, url_for, flash, redirect, send_from_directory
from room import app, db
from models import User, Miis
from flask_login import login_required, logout_user
from forms import LoginForm, KillMii, ConciergeForm
from flask_login import current_user, login_user

enabled = """
             _           _                          _     _          _   
           | |         (_)                        | |   | |        | |  
   __ _  __| |_ __ ___  _ _ __     ___ _ __   __ _| |__ | | ___  __| |  
  / _` |/ _` | '_ ` _ \| | '_ \   / _ \ '_ \ / _` | '_ \| |/ _ \/ _` |  
 | (_| | (_| | | | | | | | | | | |  __/ | | | (_| | |_) | |  __/ (_| |_ 
  \__,_|\__,_|_| |_| |_|_|_| |_|  \___|_| |_|\__,_|_.__/|_|\___|\__,_(_)
"""

# For security, the underground is disabled by default.
# To activate it, set enabled to true within config.py.
if underground_enabled:
    print(enabled)
    print("!! WARNING !!")
    print("You have entered the underground.")
    print("Changes made within the underground are potentially destructive")

    @app.route("/theunderground/login", methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for("admin"))

        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash("Invalid username or password")
            else:
                login_user(user, remember=False)
                return redirect(url_for("admin"))

        return render_template("login.html", form=form)

    @app.route("/theunderground/common.css")
    def common_css():
        return send_from_directory("templates", "common.css")

    @app.route("/theunderground/admin")
    @login_required
    def admin():
        return render_template("underground.html")

    @app.route("/theunderground/concierge")
    @login_required
    def list_concierge():
        miis = Miis.query.all()

        return render_template("concierge.html", miis=miis, mii_count=len(miis))

    @app.route("/theunderground/concierge/add")
    @login_required
    def add_concierge():
        miis = Miis.query.all()

        return render_template("concierge.html", miis=miis, mii_count=len(miis))

    @app.route("/theunderground/concierge/<mii_id>", methods=["GET", "POST"])
    @login_required
    def edit_concierge(mii_id):
        form = ConciergeForm()
        if form.validate_on_submit():
            dateformat = "%Y-%m-%dT%H:%M:%S"
            # mii = ConciergeMii(
            #     mii_id=form.miiid.data,
            #     title=form.title.data,
            #     color1=form.color1.data,
            #     color2=form.color2.data,
            #     message1=form.message1.data,
            #     message2=form.message2.data,
            #     message3=form.message3.data,
            #     message4=form.message4.data,
            #     message5=form.message5.data,
            #     message6=form.message6.data,
            #     message7=form.message7.data,
            #     updated=datetime.datetime.now().strftime(dateformat),
            #     movieid=form.movieid.data,
            # )
            # db.session.add(mii)
            # db.session.commit()
        return render_template("concierge.html", form=form)

    @app.route("/theunderground/removeconcierge")
    @login_required
    def removeconcierge():
        form = KillMii()
        return render_template("killmii.html", form=form)

    @app.route("/theunderground/logout")
    @login_required
    def process_logout():
        logout_user()
        return redirect(url_for("login"))

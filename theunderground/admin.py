from config import underground_enabled
from flask import render_template, url_for, flash, redirect, send_from_directory
from room import app, db
from models import User, ConciergeMiis, MiiMsgInfo, MiiData
from flask_login import login_required, logout_user
from forms import LoginForm, KillMii, ConciergeForm, MiiUploadForm
from flask_login import current_user, login_user
import crc16

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

    @app.route("/theunderground")
    @app.route("/theunderground/")
    def root():
        return redirect(url_for("login"))

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
        concierge_miis = ConciergeMiis.query.all()

        return render_template("concierge.html", miis=concierge_miis)

    @app.route("/theunderground/miis")
    @login_required
    def list_miis():
        miis = MiiData.query.all()

        return render_template("list_miis.html", miis=miis)

    @app.route("/theunderground/miis/add", methods=["GET", "POST"])
    @login_required
    def add_mii():
        form = MiiUploadForm()
        if form.validate_on_submit():
            mii = form.mii.data
            if mii:
                data = mii.read()
                mii_length = len(data)

                # An uploaded Mii can be with or without its checksum.
                # We'll insert one ourselves all the same.
                if mii_length == 74 or mii_length == 76:
                    # If we do have a checksum, split it off.
                    real_data = data[:74]
                    checksum = crc16.crc16xmodem(real_data).to_bytes(
                        length=2, byteorder="big"
                    )

                    # Insert this to the database.
                    full_mii = real_data + checksum
                    insert_row = MiiData(data=full_mii)
                    db.session.add(insert_row)
                    db.session.commit()
                    return redirect(url_for("list_miis"))
                else:
                    flash("Invalid Mii uploaded")
            else:
                flash("Error uploading Mii")

        return render_template("add_mii.html", form=form)

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
        return render_template("edit_concierge.html", form=form)

    @app.route("/theunderground/concierge/<mii_id>/remove", methods=["GET", "POST"])
    @login_required
    def remove_concierge(mii_id):
        form = KillMii()
        if form.validate_on_submit():
            # While this is easily circumvented, we need the user to pay attention.
            if form.given_mii_id.data == mii_id:
                db.session.delete(ConciergeMiis.query.filter_by(mii_id=mii_id).first())
                db.session.delete(MiiMsgInfo.query.filter_by(mii_id=mii_id).first())
                db.session.commit()
                return redirect("/theunderground/concierge")
            else:
                flash("Incorrect Mii ID!")
        return render_template("delete_concierge.html", form=form, mii_id=mii_id)

    @app.route("/theunderground/parade", methods=["GET", "POST"])
    @login_required
    def parade():
        form = ParadeForm()
        if form.validate_on_submit():
            parademii = ParadeMii(
                miiid=form.miiid.data,
                logo1id=form.logo1id.data,
                logobin=form.logobin.data,
            )
            db.session.add(parademii)
            db.session.commit()

    @app.route("/theunderground/logout")
    @login_required
    def process_logout():
        logout_user()
        return redirect(url_for("login"))

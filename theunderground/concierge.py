from io import BytesIO

from flask import render_template, url_for, redirect, request

from models import db, ConciergeMiis, MiiMsgInfo, MiiData, ConciergeMovies, Movies
from room import app
from theunderground.forms import ConciergeForm, ConciergeMovieForm, ConciergeMiiActions
from theunderground.operations import manage_delete_item
from theunderground.admin import oidc
from theunderground.encodemii import encode_mii_category
from room import s3
from url1.event_today import event_today
from url1.mii import obtain_mii, mii_met
from werkzeug import exceptions
from asset_data import NormalCategoryAsset
from url1.category_search import list_category_search
from theunderground.logging import log_action

import config
import requests


@app.route("/theunderground/concierge")
@oidc.require_login
def list_concierge():
    concierge_miis = (
        db.session.query(ConciergeMiis, MiiData)
        .filter(ConciergeMiis.mii_id == MiiData.mii_id)
        .all()
    )

    return render_template(
        "concierge_list.html",
        miis=concierge_miis,
        type_length=len(concierge_miis),
        type_max_count=20,
    )


@app.route("/theunderground/concierge/<mii_id>/add", methods=["GET", "POST"])
@oidc.require_login
def add_concierge(mii_id):
    form = ConciergeForm()

    if request.method == "POST":
        try:
            # Get the action value as an integer
            action_value = request.form.get("action")
            print(f"Action value: {action_value}", "debug")

            # Convert integer to enum instance
            action_enum = ConciergeMiiActions(int(action_value))

            # Create concierge data with enum instance
            concierge_data = ConciergeMiis(
                mii_id=mii_id,
                clothes=1,
                action=action_enum,  # Use the enum instance instead of int
                prof=request.form.get("prof", ""),
                movie_id=request.form.get("movieid", ""),
                voice=False,
            )

            concierge_movie = ConciergeMovies(
                mii_id=mii_id,
                movie_id=request.form.get("movieid", ""),
            )

            # Process message sequences for all 7 types
            for message_type in range(1, 8):
                seq_num = 1
                while True:
                    message_name = f"message{message_type}_{seq_num}"

                    if (
                        message_name not in request.form
                        or not request.form[message_name].strip()
                    ):
                        break

                    face_name = f"face{message_type}_{seq_num}"
                    face_value = int(request.form.get(face_name, 1))

                    # Create message entry
                    msg = MiiMsgInfo(
                        mii_id=mii_id,
                        type=message_type,
                        msg=request.form[message_name],
                        face=face_value,
                        seq=seq_num,
                    )
                    db.session.add(msg)

                    seq_num += 1

                # If no sequences were found for this type and it's not type 1, add an empty message
                if seq_num == 1 and message_type > 1:
                    msg = MiiMsgInfo(
                        mii_id=mii_id,
                        type=message_type,
                        msg="",
                        face=1,  # Default to neutral
                        seq=1,
                    )
                    db.session.add(msg)

                # Error if no messages for type 1
                if message_type == 1 and seq_num == 1:
                    print(
                        "At least one message is required for message type 1", "error"
                    )
                    return render_template(
                        "concierge_action.html", form=form, action="Add"
                    )

            # Create the category image
            mii_data = MiiData.query.filter_by(mii_id=mii_id).first()
            if not mii_data:
                return exceptions.NotFound()

            # Request the PNG from Nintendo
            mii_img = requests.get(
                f"https://miicontestp.wii.rc24.xyz/cgi-bin/render.cgi?data={mii_data.data.hex()}"
            )

            img = encode_mii_category(mii_img.content)
            # We assign concierge categories IDs 20000 - 29999.
            NormalCategoryAsset(20000 + int(mii_id)).encode(img)

            db.session.add(concierge_movie)
            db.session.add(concierge_data)
            db.session.commit()

            log_action(f"Concierge Mii {concierge_data.mii_id} added")
            update_mii_on_s3(mii_id)
            print("Concierge created successfully!", "success")
            return redirect(url_for("list_concierge"))

        except Exception as e:
            db.session.rollback()
            # Log the error for debugging
            app.logger.error(f"Error saving concierge: {str(e)}")
            # Flash a user-friendly message
            print(f"Error saving concierge: {str(e)}", "error")

    return render_template("concierge_action.html", form=form, action="Add")


@app.route("/theunderground/concierge/<mii_id>/edit", methods=["GET", "POST"])
@oidc.require_login
def edit_concierge(mii_id):
    form = ConciergeForm()
    form.submit.label.text = "Edit"

    # Get current data
    retrieved_data = (
        db.session.query(ConciergeMiis, MiiMsgInfo)
        .filter(ConciergeMiis.mii_id == mii_id)
        .filter(ConciergeMiis.mii_id == MiiMsgInfo.mii_id)
        .order_by(MiiMsgInfo.type)
        .order_by(MiiMsgInfo.seq)
        .all()
    )

    if not retrieved_data:
        return exceptions.NotFound()

    # The above query returns a list with the first index being the Concierge Mii, and the rest being the messages.
    mii_msg_infos = retrieved_data

    if form.validate_on_submit():
        mii_msg_infos[0][0].action = form.action.data
        mii_msg_infos[0][0].prof = form.prof.data
        mii_msg_infos[0][0].movie_id = form.movieid.data

        for _, info in mii_msg_infos:
            info.msg = form[f"message{info.type}"].data

        db.session.commit()

        update_mii_on_s3(mii_id)
        log_action(f"Concierge Mii {retrieved_data[0][0].mii_id} added")
        return redirect(url_for("list_concierge"))
    else:
        # Populate the data
        form.action.data = mii_msg_infos[0][0].action
        form.prof.data = mii_msg_infos[0][0].prof
        form.movieid.data = mii_msg_infos[0][0].movie_id
        for _, info in mii_msg_infos:
            form[f"message{info.type}"].data = info.msg

    return render_template("concierge_action.html", form=form, action="Edit")


@app.route("/theunderground/concierge/<mii_id>/remove", methods=["GET", "POST"])
@oidc.require_login
def remove_concierge(mii_id):
    def drop_concierge():
        concierge = ConciergeMiis.query.filter_by(mii_id=mii_id).first()
        if concierge:
            db.session.delete(concierge)

        MiiMsgInfo.query.filter_by(mii_id=mii_id).delete()
        ConciergeMovies.query.filter_by(mii_id=mii_id).delete()
        db.session.commit()

        log_action(f"Concierge Mii {mii_id} added")
        NormalCategoryAsset(20000 + int(mii_id)).delete()
        return redirect(url_for("list_concierge"))

    return manage_delete_item(mii_id, "Concierge Mii", drop_concierge)


def update_mii_on_s3(mii_id):
    if s3:
        # Update the today.xml
        event_xml = event_today()
        s3.upload_fileobj(BytesIO(event_xml), config.r2_bucket_name, "event/today.xml")

        # Metadata
        met = mii_met(mii_id)
        s3.upload_fileobj(BytesIO(met), config.r2_bucket_name, f"mii/{mii_id}.met")

        # Actual Mii
        mii = obtain_mii(mii_id)
        s3.upload_fileobj(BytesIO(mii), config.r2_bucket_name, f"mii/{mii_id}.mii")


@app.route("/theunderground/concierge/<mii_id>/movies", methods=["GET", "POST"])
@oidc.require_login
def list_concierge_movies(mii_id):
    page_num = request.args.get("page", default=1, type=int)

    movies = (
        db.session.query(ConciergeMovies, Movies)
        .filter(ConciergeMovies.movie_id == Movies.movie_id)
        .filter(ConciergeMovies.mii_id == mii_id)
        .paginate(page=page_num, per_page=20, error_out=False)
    )

    return render_template(
        "concierge_movies_list.html",
        mii_id=mii_id,
        movies=movies,
        type_length=movies.total,
        type_max_count=20,
    )


@app.route("/theunderground/concierge/<mii_id>/movies/add", methods=["GET", "POST"])
@oidc.require_login
def add_concierge_movie(mii_id):
    form = ConciergeMovieForm()
    if form.validate_on_submit():
        movie = ConciergeMovies(movie_id=form.movie_id.data, mii_id=int(mii_id))
        db.session.add(movie)
        db.session.commit()

        # Finally update the category if needed by S3
        if s3:
            cat_xml = list_category_search(20000 + int(mii_id))
            xml_path = f"list/category/search/{20000 + int(mii_id)}"
            s3.upload_fileobj(BytesIO(cat_xml), config.r2_bucket_name, xml_path)

        log_action(f"Concierge Mii {mii_id}'s movie with ID {form.movie_id.data} added")
        return redirect(url_for("list_concierge_movies", mii_id=mii_id))

    return render_template("concierge_movie_add.html", form=form)


@app.route(
    "/theunderground/concierge/<mii_id>/movies/<movie_id>/remove",
    methods=["GET", "POST"],
)
@oidc.require_login
def remove_concierge_movie(mii_id, movie_id):
    def drop_concierge_movie():
        db.session.delete(
            ConciergeMovies.query.filter_by(mii_id=mii_id)
            .filter_by(movie_id=movie_id)
            .first()
        )
        db.session.commit()

        # Reflect the change in the category
        if s3:
            cat_xml = list_category_search(20000 + int(mii_id))
            xml_path = f"list/category/search/{20000 + int(mii_id)}"
            s3.upload_fileobj(BytesIO(cat_xml), config.r2_bucket_name, xml_path)

        log_action(f"Concierge Mii {mii_id}'s movie with ID {movie_id} added")
        return redirect(url_for("list_concierge"))

    return manage_delete_item(movie_id, "Concierge Mii Movie", drop_concierge_movie)

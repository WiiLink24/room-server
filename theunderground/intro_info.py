from io import BytesIO


from flask import (
    render_template,
    request,
    flash,
    redirect,
    url_for,
    send_from_directory,
)
from asset_data import TVScreenAsset
from room import app, s3
from models import IntroInfo, db, ContentTypes
from theunderground.forms import IntroInfoForm
from theunderground.mobiclip import validate_mobiclip
from theunderground.operations import manage_delete_item
from theunderground.admin import oidc
from theunderground.locale import get_current_locale
from werkzeug import exceptions
from url1.event_today import event_today
from theunderground.logging import log_action
from flask_wtf.file import FileRequired

import config


@app.route("/theunderground/intro_info")
@oidc.require_login
def list_intro_info():
    page_num = request.args.get("page", default=1, type=int)

    infos = (
        db.session.query(IntroInfo)
        .where(IntroInfo.locale == get_current_locale())
        .order_by(IntroInfo.position.asc())
        .paginate(page=page_num, per_page=15, error_out=False)
    )

    return render_template(
        "intro_info_list.html", infos=infos, type_length=infos.total, type_max_count=30
    )


@app.route("/theunderground/intro_info/move/<position>/<direction>")
@oidc.require_login
def move_info(position, direction):
    position = int(position)
    if direction == "up":
        # We require the current banner and the one before it.
        infos = (
            db.session.query(IntroInfo)
            .filter(IntroInfo.position.between(position - 1, position))
            .where(IntroInfo.locale == get_current_locale())
            .order_by(IntroInfo.position.asc())
            .all()
        )
        infos[0].position += 1
        infos[1].position -= 1
    elif direction == "down":
        # We require the current banner and the one after it.
        infos = (
            db.session.query(IntroInfo)
            .filter(IntroInfo.position.between(position, position + 1))
            .where(IntroInfo.locale == get_current_locale())
            .order_by(IntroInfo.position.asc())
            .all()
        )
        infos[0].position += 1
        infos[1].position -= 1

    db.session.commit()
    return redirect(url_for("list_intro_info", l=get_current_locale()))


@app.route("/theunderground/intro_info/add", methods=["GET", "POST"])
@oidc.require_login
def add_intro_info():
    form = IntroInfoForm()
    form.asset.validators = [FileRequired()]

    if form.is_submitted():
        # Get next position for current locale
        position = (
            db.session.query(IntroInfo)
            .where(IntroInfo.locale == form.locale.data)
            .count()
            + 1
        )
        intro_db = IntroInfo(
            position=position,
            cnt_type=form.cnt_type.data,
            link_type=form.link_type.data,
            locale=form.locale.data,
        )

        if form.cat_name:
            intro_db.cat_name = form.cat_name.data

        if form.link_id:
            intro_db.link_id = form.link_id.data

        # Now push to database.
        db.session.add(intro_db)
        db.session.commit()

        # Wii Room requires video content id's to be 16 characters long.
        if intro_db.cnt_type == ContentTypes.Video:
            intro_db.cnt_id = int(str(intro_db.cnt_id).ljust(16, "0"))
            db.session.add(intro_db)
            db.session.commit()

        update_intro_info_on_s3()

        # Now encode image/video.
        if form.asset.data:
            if intro_db.cnt_type == ContentTypes.Image:
                TVScreenAsset(intro_db.cnt_id, is_theatre=False, is_movie=False).encode(
                    form.asset
                )
            else:
                video = form.asset.data.read()
                if validate_mobiclip(video):
                    TVScreenAsset(
                        intro_db.cnt_id, is_theatre=False, is_movie=True
                    ).upload_movie(video)
                else:
                    flash("Invalid movie!")
        else:
            flash("Error uploading asset!")

        log_action(f"Intro Info {intro_db.cnt_id} was added")
        return redirect(url_for("list_intro_info", l=form.locale.data))

    return render_template("intro_info_action.html", form=form, action="Add")


@app.route("/theunderground/intro_info/<id>/edit", methods=["GET", "POST"])
@oidc.require_login
def edit_intro_info(id):
    current_info = db.session.query(IntroInfo).filter(IntroInfo.cnt_id == id).first()
    if not current_info:
        return exceptions.NotFound()

    form = IntroInfoForm()

    if form.is_submitted():
        current_info.cnt_type = form.cnt_type.data
        current_info.link_type = form.link_type.data
        current_info.cat_name = form.cat_name.data
        current_info.link_id = form.link_id.data

        # If the locale changes, we have to also change the positioning of the info we are editing, as well as everything after it.
        if form.locale.data != current_info.locale:
            infos = (
                db.session.query(IntroInfo)
                .where(IntroInfo.locale == current_info.locale)
                .filter(IntroInfo.position > current_info.position)
                .all()
            )
            for info in infos:
                info.position -= 1

            position = (
                db.session.query(IntroInfo)
                .where(IntroInfo.locale == form.locale.data)
                .count()
                + 1
            )
            current_info.position = position
            current_info.locale = form.locale.data

        # Wii Room requires video content id's to be 16 characters long.
        if current_info.cnt_type == ContentTypes.Video:
            current_info.cnt_id = int(str(current_info.cnt_id).ljust(16, "0"))

        db.session.commit()
        update_intro_info_on_s3()

        # Now encode image/video.
        if form.asset.data:
            if current_info.cnt_type == ContentTypes.Image:
                TVScreenAsset(
                    current_info.cnt_id, is_theatre=False, is_movie=False
                ).encode(form.asset)
            else:
                video = form.asset.data.read()
                if validate_mobiclip(video):
                    TVScreenAsset(
                        current_info.cnt_id, is_theatre=False, is_movie=True
                    ).upload_movie(video)
                else:
                    flash("Invalid movie!")

        log_action(f"Intro Info {current_info.cnt_id} was edited")
        return redirect(url_for("list_intro_info", l=form.locale.data))
    else:
        form.cnt_type.data = current_info.cnt_type
        form.link_type.data = current_info.link_type
        form.link_id.data = current_info.link_id
        form.cat_name.data = current_info.cat_name
        form.locale.data = current_info.locale

    return render_template("intro_info_action.html", form=form, action="Edit")


@app.route("/theunderground/intro_info/<id>/remove", methods=["GET", "POST"])
@oidc.require_login
def remove_intro_info(id):
    def drop_intro_info():
        # All positioning after the current info needs to be updated.
        infos = (
            db.session.query(IntroInfo)
            .where(IntroInfo.locale == current_info.locale)
            .filter(IntroInfo.position > current_info.position)
            .all()
        )
        for info in infos:
            info.position -= 1

        db.session.delete(current_info)
        db.session.commit()

        log_action(f"Intro Info {id} was removed")
        return redirect(url_for("list_intro_info"))

    current_info = db.session.query(IntroInfo).filter(IntroInfo.cnt_id == id).first()
    if not current_info:
        return exceptions.NotFound()

    return manage_delete_item(id, "info intro", drop_intro_info)


def update_intro_info_on_s3():
    # Regenerate event/today.xml on s3 if needed
    if s3:
        event_xml = event_today()
        s3.upload_fileobj(BytesIO(event_xml), config.r2_bucket_name, "event/today.xml")


@app.route("/theunderground/intro_info/<cnt_id>/thumbnail.jpg")
@oidc.require_login
def get_info_image(cnt_id):
    if s3:
        return redirect(f"{config.url1_cdn_url}/normal-intro/{cnt_id}-1.img")

    return send_from_directory("assets/normal-intro/", f"{cnt_id}-1.img")

from flask import (
    render_template,
    redirect,
    flash,
    send_from_directory,
    request,
    url_for,
)
from flask_wtf.file import FileRequired
from werkzeug import exceptions

from models import Movies, db
from room import app
from theunderground.mobiclip import (
    get_category_list,
    validate_mobiclip,
    validate_mobi_dsi,
    get_mobiclip_length,
    save_movie_data,
    delete_movie_data,
    get_movie_path,
    get_ds_movie_path,
    get_room_list,
)
from theunderground.forms import MovieUploadForm
from theunderground.operations import manage_delete_item
from theunderground.admin import oidc
from room import s3
import config
from url1.category_search import list_category_search
from theunderground.logging import log_action
from io import BytesIO


@app.route("/theunderground/categories/<category>")
@oidc.require_login
def list_movies(category):
    # Get our current page, or start from scratch.
    page_num = request.args.get("page", default=1, type=int)

    # We want at most 20 movies per page.
    movies = Movies.query.filter(Movies.category_id == category).paginate(
        page=page_num, per_page=20, error_out=False
    )

    unlisted_movies = (
        Movies.query.filter(Movies.category_id == category)
        .filter(Movies.unlisted == True)
        .all()
    )

    return render_template(
        "movie_list.html",
        movies=movies,
        category_id=category,
        type_length=movies.total - len(unlisted_movies),
        type_max_count=64,
    )


@app.route("/theunderground/movies/<category>/<movie_id>/listed")
def toggle_movie_listed(category, movie_id):
    movie = Movies.query.filter_by(movie_id=movie_id).first()
    movie.unlisted = not movie.unlisted
    db.session.commit()
    return redirect(url_for("list_movies", category=category))


@app.route("/theunderground/movies/add", methods=["GET", "POST"])
@oidc.require_login
def add_movie():
    form = MovieUploadForm()
    form.category.choices = get_category_list()
    form.room.choices = get_room_list()
    form.movie.validators = [FileRequired()]
    form.thumbnail.validators = [FileRequired()]

    if form.validate_on_submit():
        movie = form.movie.data
        ds_movie = form.ds_movie.data
        thumbnail = form.thumbnail.data
        if movie and thumbnail:
            movie_data = movie.read()
            thumbnail_data = thumbnail.read()
            ds_movie_data = None

            if validate_mobiclip(movie_data):
                # Get the Mobiclip's length from header.
                length = get_mobiclip_length(movie_data)

                # Insert this movie to the database.
                # For right now, we will assume defaults.
                db_movie = Movies(
                    title=form.title.data,
                    category_id=form.category.data,
                    length=length,
                    aspect=True,
                    genre=form.genre.data,
                    sp_page_id=form.room.data,
                    staff=False,
                )

                db.session.add(db_movie)
                db.session.commit()

                if ds_movie:
                    ds_movie_data = ds_movie.read()
                    validation_ds = validate_mobi_dsi(ds_movie_data)
                    if isinstance(validation_ds, bytes):
                        # We encrypted this movie.
                        ds_movie_data = validation_ds

                    if validation_ds:
                        db_movie.ds_mov_id = db_movie.movie_id
                        # Re-commit the DSi stuff
                        db.session.commit()

                # Now that we've inserted the movie, we can properly move it.
                save_movie_data(
                    db_movie.movie_id, thumbnail_data, movie_data, ds_movie_data
                )

                # Finally update the category if needed by S3
                if s3:
                    cat_xml = list_category_search(form.category.data)
                    xml_path = f"list/category/search/{form.category.data}"
                    s3.upload_fileobj(BytesIO(cat_xml), config.r2_bucket_name, xml_path)

                log_action(f"Movie ID {db_movie.movie_id} added")
                return redirect(url_for("list_categories"))
            else:
                flash("Invalid movie!")
        else:
            flash("Error uploading movie!")

    return render_template("movie_action.html", form=form, action="Add")


@app.route("/theunderground/movies/<movie_id>/edit", methods=["GET", "POST"])
@oidc.require_login
def edit_movie(movie_id):
    form = MovieUploadForm()
    form.category.choices = get_category_list()
    form.room.choices = get_room_list()
    form.upload.label.text = "Edit"

    movie = Movies.query.filter_by(movie_id=movie_id).first()
    if not movie:
        return exceptions.NotFound()

    if form.validate_on_submit():
        thumbnail_data = None
        movie_data = None
        ds_movie_data = None
        if form.movie.data:
            movie_data = form.movie.data.read()
            if validate_mobiclip(movie_data):
                length = get_mobiclip_length(movie_data)
                movie.length = length
            else:
                flash("Invalid movie")
                return render_template("movie_action.html", form=form, action="Edit")

        if form.thumbnail.data:
            thumbnail_data = form.thumbnail.data.read()

        if form.ds_movie.data:
            ds_movie_data = form.ds_movie.data.read()
            validation_ds = validate_mobi_dsi(ds_movie_data)
            if isinstance(validation_ds, bytes):
                # We encrypted this movie.
                ds_movie_data = validation_ds

            if not validation_ds:
                flash("Invalid DS movie")
                return render_template("movie_action.html", form=form, action="Edit")

            movie.ds_mov_id = movie.movie_id

        save_movie_data(movie.movie_id, thumbnail_data, movie_data, ds_movie_data)

        # Finally update the title, genre and category.
        movie.title = form.title.data
        movie.genre = form.genre.data
        movie.category_id = form.category.data
        movie.sp_page_id = form.room.data
        db.session.commit()

        if s3:
            cat_xml = list_category_search(form.category.data)
            xml_path = f"list/category/search/{form.category.data}"
            s3.upload_fileobj(BytesIO(cat_xml), config.r2_bucket_name, xml_path)

        log_action(f"Movie ID {movie_id} edited")
        return redirect(url_for("list_categories"))
    else:
        form.title.data = movie.title
        form.genre.data = movie.genre
        form.category.data = movie.category_id

    return render_template(
        "movie_action.html", form=form, action="Edit", movie_id=movie_id
    )


@app.route("/theunderground/movies/<movie_id>/save", methods=["GET", "POST"])
@oidc.require_login
def save_movie(movie_id):
    movie_dir = get_movie_path(movie_id)
    if s3:
        return redirect(f"{config.url1_cdn_url}/{movie_dir}/{movie_id}-H.mov")

    return send_from_directory(movie_dir, f"{movie_id}-H.mov")


@app.route("/theunderground/movies/<movie_id>/save_ds", methods=["GET", "POST"])
@oidc.require_login
def save_ds_movie(movie_id):
    ds_movie_dir = get_ds_movie_path(movie_id)
    if s3:
        return redirect(f"{config.url1_cdn_url}/{ds_movie_dir}/{movie_id}.enc")

    return send_from_directory(ds_movie_dir, f"{movie_id}.enc")


@app.route("/theunderground/movies/<movie_id>/remove", methods=["GET", "POST"])
@oidc.require_login
def remove_movie(movie_id):
    def drop_movie():
        movie = Movies.query.filter_by(movie_id=movie_id).first()
        has_ds = movie.ds_mov_id is not None
        db.session.delete(movie)
        db.session.commit()

        delete_movie_data(movie_id, has_ds)

        log_action(f"Movie ID {movie_id} removed")
        return redirect(url_for("list_categories"))

    return manage_delete_item(movie_id, "movie", drop_movie)


@app.route("/theunderground/movies/<movie_id>/thumbnail.jpg")
@oidc.require_login
def get_movie_thumbnail(movie_id):
    movie_dir = get_movie_path(movie_id)
    if s3:
        return redirect(f"{config.url1_cdn_url}/{movie_dir}/{movie_id}.img")

    return send_from_directory(movie_dir, f"{movie_id}.img")

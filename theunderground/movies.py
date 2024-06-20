from flask import (
    render_template,
    redirect,
    flash,
    send_from_directory,
    request,
    url_for,
)


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
    get_ds_movie_path
)
from theunderground.forms import MovieUploadForm
from theunderground.operations import manage_delete_item
from theunderground.admin import oidc
from room import s3
import config
from url1.category_search import list_category_search
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

    return render_template(
        "movie_list.html",
        movies=movies,
        category_id=category,
        type_length=movies.total,
        type_max_count=64,
    )


@app.route("/theunderground/movies/add", methods=["GET", "POST"])
@oidc.require_login
def add_movie():
    form = MovieUploadForm()
    form.category.choices = get_category_list()

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

                if form.is_collab.data:
                    genre = 2
                else:
                    genre = 0

                # Insert this movie to the database.
                # For right now, we will assume defaults.
                db_movie = Movies(
                    title=form.title.data,
                    category_id=form.category.data,
                    length=length,
                    aspect=True,
                    genre=genre,
                    sp_page_id=0,
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
                        if genre == 0:
                            db_movie.genre = 1

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

                return redirect(url_for("list_categories"))
            else:
                flash("Invalid movie!")
        else:
            flash("Error uploading movie!")

    return render_template("movie_add.html", form=form)


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
        db.session.delete(Movies.query.filter_by(movie_id=movie_id).first())
        db.session.commit()

        delete_movie_data(movie_id)

        return redirect(url_for("list_categories"))

    return manage_delete_item(movie_id, "movie", drop_movie)


@app.route("/theunderground/movies/<movie_id>/thumbnail.jpg")
@oidc.require_login
def get_movie_thumbnail(movie_id):
    movie_dir = get_movie_path(movie_id)
    if s3:
        return redirect(f"{config.url1_cdn_url}/{movie_dir}/{movie_id}.img")

    return send_from_directory(movie_dir, f"{movie_id}.img")

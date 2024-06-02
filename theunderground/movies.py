from flask import (
    render_template,
    redirect,
    flash,
    send_from_directory,
    request,
    url_for,
)
from flask_login import login_required

from models import Movies, db
from room import app
from theunderground.mobiclip import (
    get_category_list,
    validate_mobiclip,
    get_mobiclip_length,
    save_movie_data,
    delete_movie_data,
    get_movie_path,
)
from theunderground.forms import MovieUploadForm
from theunderground.operations import manage_delete_item
from room import s3
import config
from url1.category_search import list_category_search
from io import BytesIO


@app.route("/theunderground/categories/<category>")
@login_required
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
@login_required
def add_movie():
    form = MovieUploadForm()
    form.category.choices = get_category_list()

    if form.validate_on_submit():
        movie = form.movie.data
        dsmovie = form.dsmovie.data
        thumbnail = form.thumbnail.data
        if movie and thumbnail:
            movie_data = movie[0].read()
            thumbnail_data = thumbnail[0].read()

            if dsmovie:
                dsmovie_data = dsmovie[0].read()
                ds_mov_id = 2
                genre = 1
            else:
                ds_mov_id = None
                genre = 0

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
                    genre=genre,
                    sp_page_id=0,
                    ds_mov_id=ds_mov_id,
                    staff=False,
                )

                db.session.add(db_movie)
                db.session.commit()

                # Now that we've inserted the movie, we can properly move it.
                save_movie_data(db_movie.movie_id, thumbnail_data, movie_data)

                # Save the DS movie if it exists to /dsmov/{get_movie_path}/{movie_id}.enc
                # NOT on s3

                if dsmovie:
                    dsmovie_dir = get_movie_path(db_movie.movie_id)
                    dsmovie_path = f"{dsmovie_dir}/{db_movie.movie_id}.enc"

                    with open(dsmovie_path, "wb") as f:
                        f.write(dsmovie_data)

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


@app.route("/theunderground/movies/<movie_id>/remove", methods=["GET", "POST"])
@login_required
def remove_movie(movie_id):
    def drop_movie():
        db.session.delete(Movies.query.filter_by(movie_id=movie_id).first())
        db.session.commit()

        delete_movie_data(movie_id)

        return redirect(url_for("list_categories"))

    return manage_delete_item(movie_id, "movie", drop_movie)


@app.route("/theunderground/movies/<movie_id>/thumbnail.jpg")
@login_required
def get_movie_thumbnail(movie_id):
    movie_dir = get_movie_path(movie_id)
    if s3:
        return redirect(f"{config.url1_cdn_url}/{movie_dir}/{movie_id}.img")

    return send_from_directory(movie_dir, f"{movie_id}.img")

from flask import render_template, redirect, flash, send_from_directory, request
from flask_login import login_required

from config import video_deletion_enabled
from models import Movies, CategoryMovies
from room import app, db, es
from theunderground.mobiclip import (
    get_category_list,
    validate_mobiclip,
    get_mobiclip_length,
    save_movie_data,
    delete_movie_data,
    get_movie_dir,
)
from theunderground.forms import KillMii, MovieUploadForm


@app.route("/theunderground/movies")
@login_required
def list_movies():
    # Get our current page, or start from scratch.
    page_num = request.args.get("page", default=1, type=int)

    # We want at most 20 movies per page.
    movies = Movies.query.order_by(Movies.movie_id.asc()).paginate(
        page_num, 20, error_out=False
    )

    return render_template(
        "movie_list.html",
        movies=movies,
        video_deletion_enabled=video_deletion_enabled,
        type_length=movies.total,
    )


@app.route("/theunderground/movies/add", methods=["GET", "POST"])
@login_required
def add_movie():
    form = MovieUploadForm()
    form.category.choices = get_category_list()

    if form.validate_on_submit():
        movie = form.movie.data
        thumbnail = form.thumbnail.data
        if movie and thumbnail:
            movie_data = movie.read()
            thumbnail_data = thumbnail.read()

            if validate_mobiclip(movie_data):
                # Get the Mobiclip's length from header.
                length = get_mobiclip_length(movie_data)

                # Insert this movie to the database.
                # For right now, we will assume defaults.
                db_movie = Movies(
                    title=form.title.data,
                    length=length,
                    aspect=True,
                    genre=0,
                    sp_page_id=0,
                    ds_dist=False,
                    staff=False,
                )

                db.session.add(db_movie)
                db.session.commit()

                db.session.add(
                    CategoryMovies(
                        category_id=form.category.data, movie_id=db_movie.movie_id
                    )
                )
                db.session.commit()

                # Now that we've inserted the movie, we can properly move it.
                save_movie_data(db_movie.movie_id, thumbnail_data, movie_data)

                # Finally, allow it for indexing.
                es.index(
                    index="tv_index",
                    body={"title": form.title.data, "movie_id": db_movie.movie_id},
                )

                return redirect("/theunderground/movies")
            else:
                flash("Invalid movie!")
        else:
            flash("Error uploading movie!")

    return render_template("movie_add.html", form=form)


if video_deletion_enabled:

    @app.route("/theunderground/movies/<movie_id>/remove", methods=["GET", "POST"])
    @login_required
    def remove_movie(movie_id):
        form = KillMii()
        if form.validate_on_submit():
            # While this is easily circumvented, we need the user to pay attention.
            if form.given_id.data == movie_id:
                db.session.delete(
                    CategoryMovies.query.filter_by(movie_id=movie_id).first()
                )
                db.session.delete(Movies.query.filter_by(movie_id=movie_id).first())
                db.session.commit()

                delete_movie_data(movie_id)

                return redirect("/theunderground/movies")
            else:
                flash("Incorrect Mii ID!")
        return render_template("movie_delete.html", form=form, item_id=movie_id)


@app.route("/theunderground/movies/<movie_id>/thumbnail.jpg")
@login_required
def get_movie_thumbnail(movie_id):
    movie_dir = get_movie_dir(movie_id)
    return send_from_directory(movie_dir, f"{movie_id}.img")

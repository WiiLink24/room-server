from flask import render_template, redirect, flash, send_from_directory, request
from flask_login import login_required

from config import video_deletion_enabled
from models import PayMovies, CategoryPayMovies
from room import app, db, es
from theunderground.mobiclip import (
    get_pay_category_list,
    validate_mobiclip,
    get_mobiclip_length,
    save_pay_movie_data,
    delete_pay_movie_data,
    get_pay_movie_dir,
)
from theunderground.forms import KillMii, PayMovieUploadForm


@app.route("/theunderground/paycategories/<category>")
@login_required
def list_pay_movies(category):
    # Get our current page, or start from scratch.
    page_num = request.args.get("page", default=1, type=int)

    # We want at most 10 posters per page.
    movies = (
        db.session.query(PayMovies, CategoryPayMovies)
        .filter(CategoryPayMovies.category_id == category)
        .filter(CategoryPayMovies.movie_id == PayMovies.movie_id)
        .paginate(page_num, 10, error_out=False)
    )

    return render_template(
        "pay_movie_list.html",
        movies=movies,
        category_id=category,
        video_deletion_enabled=video_deletion_enabled,
        type_length=movies.total,
        type_max_count=64,
    )


@app.route("/theunderground/paymovies/add", methods=["GET", "POST"])
@login_required
def add_pay_movie():
    form = PayMovieUploadForm()
    form.category.choices = get_pay_category_list()

    if form.validate_on_submit():
        movie = form.movie.data
        poster = form.poster.data
        thumbnail = form.thumbnail.data
        if movie and poster:
            movie_data = movie.read()
            poster_data = poster.read()
            thumbnail_data = thumbnail.read()

            if validate_mobiclip(movie_data):
                # Get the Mobiclip's length from header.
                length = get_mobiclip_length(movie_data)

                # Insert this movie to the database.
                # For right now, we will assume defaults.
                db_movie = PayMovies(
                    title=form.title.data,
                    length=length,
                    note=form.note.data,
                    price=form.price.data,
                    released=form.release.data,
                )

                db.session.add(db_movie)
                db.session.commit()

                db.session.add(
                    CategoryPayMovies(
                        category_id=form.category.data, movie_id=db_movie.movie_id
                    )
                )
                db.session.commit()

                # Now that we've inserted the movie, we can properly move it.
                save_pay_movie_data(db_movie.movie_id, thumbnail_data, movie_data, poster_data)

                # Finally, allow it for indexing.
                es.index(
                    index="tv_index",
                    body={"title": form.title.data, "movie_id": db_movie.movie_id},
                )

                return redirect("/theunderground/paycategories")
            else:
                flash("Invalid movie!")
        else:
            flash("Error uploading movie!")

    return render_template("pay_movie_add.html", form=form)


if video_deletion_enabled:

    @app.route("/theunderground/paymovies/<movie_id>/remove", methods=["GET", "POST"])
    @login_required
    def remove_pay_movie(movie_id):
        form = KillMii()
        if form.validate_on_submit():
            # While this is easily circumvented, we need the user to pay attention.
            if form.given_id.data == movie_id:
                db.session.delete(
                    CategoryPayMovies.query.filter_by(movie_id=movie_id).first()
                )
                db.session.delete(PayMovies.query.filter_by(movie_id=movie_id).first())
                db.session.commit()

                delete_pay_movie_data(movie_id)

                return redirect("/theunderground/paycategories")
            else:
                flash("Incorrect Mii ID!")
        return render_template("pay_movie_delete.html", form=form, item_id=movie_id)


@app.route("/theunderground/paymovies/<movie_id>/thumbnail.jpg")
@login_required
def get_movie_poster(movie_id):
    movie_dir = get_pay_movie_dir(movie_id)
    return send_from_directory(movie_dir, f"{movie_id}/{movie_id}.img")


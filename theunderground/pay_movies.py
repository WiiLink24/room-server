from flask import (
    render_template,
    redirect,
    flash,
    send_from_directory,
    request,
    url_for,
)


from models import PayMovies, db
from room import app
from theunderground.mobiclip import (
    get_pay_category_list,
    validate_mobiclip,
    validate_mobi_dsi,
    get_mobiclip_length,
    save_pay_movie_data,
    delete_pay_movie_data,
    get_pay_movie_dir,
    get_ds_movie_path,
)
from theunderground.forms import PayMovieUploadForm
from theunderground.operations import manage_delete_item
from theunderground.admin import oidc


@app.route("/theunderground/paycategories/<category>")
@oidc.require_login
def list_pay_movies(category):
    # Get our current page, or start from scratch.
    page_num = request.args.get("page", default=1, type=int)

    # We want at most 10 posters per page.
    movies = PayMovies.query.filter(PayMovies.category_id == category).paginate(
        page=page_num, per_page=20, error_out=False
    )

    return render_template(
        "pay_movie_list.html",
        movies=movies,
        category_id=category,
        type_length=movies.total,
        type_max_count=64,
    )


@app.route("/theunderground/paymovies/add", methods=["GET", "POST"])
@oidc.require_login
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
            ds_movie_data = None

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
                    category_id=form.category.data,
                    price_code=form.price_code.data,
                    reference_id=form.ref_id.data,
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
                save_pay_movie_data(
                    db_movie.movie_id, thumbnail_data, movie_data, poster_data
                )

                return redirect(url_for("list_pay_categories"))
            else:
                flash("Invalid movie!")
        else:
            flash("Error uploading movie!")

    return render_template("pay_movie_add.html", form=form)


@app.route("/theunderground/paymovies/<movie_id>/remove", methods=["GET", "POST"])
@oidc.require_login
def remove_pay_movie(movie_id):
    def drop_pay_movie():
        db.session.delete(PayMovies.query.filter_by(movie_id=movie_id).first())
        db.session.commit()

        delete_pay_movie_data(movie_id)

        return redirect(url_for("list_pay_categories"))

    return manage_delete_item(movie_id, "pay movie", drop_pay_movie)


@app.route("/theunderground/paymovies/<movie_id>/thumbnail.jpg")
@oidc.require_login
def get_movie_poster(movie_id):
    movie_dir = get_pay_movie_dir(movie_id)
    return send_from_directory(movie_dir, f"{movie_id}/{movie_id}.img")

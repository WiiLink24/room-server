from flask import (
    render_template,
    redirect,
    url_for,
)

from models import Movies, MovieCredits, db
from room import app
from theunderground.forms import CreditsForm
from theunderground.admin import oidc
from werkzeug import exceptions


@app.route("/theunderground/movies/<movie_id>/credits/add", methods=["GET", "POST"])
@oidc.require_login
def add_credits(movie_id):
    form = CreditsForm()
    if form.validate_on_submit():
        movie = Movies.query.filter_by(movie_id=movie_id).first()
        if movie is None:
            return exceptions.NotFound()

        # Set credits flag to true
        movie.staff = True

        order = 1
        for i in range(0, len(form.role_and_name_list.data), 2):
            db_credits = MovieCredits(
                movie_id=movie_id,
                role=form.role_and_name_list.data[i],
                name=form.role_and_name_list.data[i + 1],
                order=order,
            )

            db.session.add(db_credits)
            order += 1

        db.session.commit()
        return redirect(url_for("list_categories"))

    return render_template("credits_add.html", form=form)


@app.route("/theunderground/movies/<movie_id>/credits/edit", methods=["GET", "POST"])
@oidc.require_login
def edit_credits(movie_id):
    form = CreditsForm()

    movie = Movies.query.filter_by(movie_id=movie_id).first()
    if movie is None:
        return exceptions.NotFound()

    queried_credits = []
    if form.validate_on_submit():
        received_length = len(form.role_and_name_list.data) / 2
        original_length = MovieCredits.query.filter_by(movie_id=movie_id).count()
        if received_length < original_length:
            # If the edited credits is less than what is in the database, we must delete the removed.
            MovieCredits.query.filter_by(movie_id=movie_id).where(
                MovieCredits.order > received_length
            ).delete()

        # We can handle any edits now.
        order = 1
        for i in range(0, int(received_length) * 2, 2):
            # Query the row
            data = (
                MovieCredits.query.filter_by(movie_id=movie_id)
                .filter_by(order=order)
                .first()
            )
            if not data:
                # Brand new row.
                db_credits = MovieCredits(
                    movie_id=movie_id,
                    role=form.role_and_name_list.data[i],
                    name=form.role_and_name_list.data[i + 1],
                    order=order,
                )

                db.session.add(db_credits)
            else:
                data.role = form.role_and_name_list.data[i]
                data.name = form.role_and_name_list.data[i + 1]

            order += 1

        db.session.commit()
        return redirect(url_for("list_categories"))
    else:
        queried_credits = (
            MovieCredits.query.filter_by(movie_id=movie_id)
            .order_by(MovieCredits.order.asc())
            .all()
        )

    return render_template(
        "credits_edit.html",
        form=form,
        num_of_credits=len(queried_credits),
        credits=queried_credits,
    )

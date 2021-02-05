from flask import render_template, url_for, redirect, flash
from flask_login import login_required

from models import News
from room import app, db
from theunderground.forms import NewsForm, KillMii


@app.route("/theunderground/news")
@login_required
def list_news():
    news = News.query.all()

    return render_template("news.html", news=news)


@app.route("/theunderground/news/<id>")
@login_required
def edit_news():
    form = NewsForm()
    if form.validate_on_submit():
        # Obtain the news with that id
        news = News.query.filter_by(id=id)
        # Now we change the message
        news.news = form.news.value
        # Now commit it
        db.session.add(news)
        db.session.commit()

        return redirect(url_for("list_news"))

    return render_template("add_news.html", form=form)


@app.route("/theunderground/news/add", methods=["GET", "POST"])
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        nq = News.query.all()
        if len(nq) != 0:
            id = News.query.filter_by(id=len(nq) - 1).first().id + 1
        else:
            id = 0
        created_news = News(id=id, msg=form.news.data)
        db.session.add(created_news)
        db.session.commit()

        return redirect(url_for("list_news"))

    return render_template("add_news.html", form=form)


@app.route("/theunderground/news/<mii_id>/remove", methods=["GET", "POST"])
@login_required
def remove_news(mii_id):
    form = KillMii()
    if form.validate_on_submit():
        # While this is easily circumvented, we need the user to pay attention.
        if form.given_mii_id.data == mii_id:
            db.session.delete(News.query.filter_by(id=mii_id).first())
            db.session.commit()
            return redirect("/theunderground/news")
        else:
            flash("Incorrect news ID!")
    return render_template("delete_news.html", form=form, mii_id=mii_id)

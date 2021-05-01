from flask import render_template, url_for, redirect, flash
from flask_login import login_required
from werkzeug import exceptions

from models import News
from room import app, db
from theunderground.forms import NewsForm, KillMii


@app.route("/theunderground/news")
@login_required
def list_news():
    news = News.query.all()
    return render_template(
        "news_list.html", news=news, type_length=len(news), type_max_count=64
    )


@app.route("/theunderground/news/<news_id>", methods=["GET", "POST"])
@login_required
def edit_news(news_id):
    form = NewsForm()

    # Obtain the news with that id
    news_item = News.query.filter_by(id=news_id).first()
    if not news_item:
        return exceptions.NotFound()

    if form.validate_on_submit():
        # Now we change the message
        news_item.msg = form.news.data
        # Now commit it
        db.session.add(news_item)
        db.session.commit()

        return redirect(url_for("list_news"))

    # Populate with existing news.
    form.news.data = news_item.msg

    return render_template("news_action.html", action="Edit", form=form)


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

    return render_template("news_action.html", action="Add", form=form)


@app.route("/theunderground/news/<news_id>/remove", methods=["GET", "POST"])
@login_required
def remove_news(news_id):
    form = KillMii()
    if form.validate_on_submit():
        # While this is easily circumvented, we need the user to pay attention.
        if form.given_id.data == news_id:
            db.session.delete(News.query.filter_by(id=news_id).first())
            db.session.commit()
            return redirect(url_for("list_news"))
        else:
            flash("Incorrect news ID!")

    return render_template("news_delete.html", form=form, item_id=news_id)

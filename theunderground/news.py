from io import BytesIO

from flask import render_template, url_for, redirect

from werkzeug import exceptions

from models import News, db
from room import app, s3
from theunderground.forms import NewsForm
from theunderground.operations import manage_delete_item
from theunderground.admin import oidc
from url1.event_today import event_today
from theunderground.logging import log_action

import config


@app.route("/theunderground/news")
@oidc.require_login
def list_news():
    news = News.query.all()
    return render_template(
        "news_list.html", news=news, type_length=len(news), type_max_count=64
    )


@app.route("/theunderground/news/<news_id>", methods=["GET", "POST"])
@oidc.require_login
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

        update_news_on_s3()
        log_action(f"News {news_id} edited")
        return redirect(url_for("list_news"))

    # Populate with existing news.
    form.news.data = news_item.msg

    return render_template("news_action.html", action="Edit", form=form)


@app.route("/theunderground/news/add", methods=["GET", "POST"])
@oidc.require_login
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        created_news = News(msg=form.news.data)
        db.session.add(created_news)
        db.session.commit()

        update_news_on_s3()

        log_action(f"News {created_news.id} added")
        return redirect(url_for("list_news"))

    return render_template("news_action.html", action="Add", form=form)


@app.route("/theunderground/news/<news_id>/remove", methods=["GET", "POST"])
@oidc.require_login
def remove_news(news_id):
    def drop_news():
        db.session.delete(News.query.filter_by(id=news_id).first())
        db.session.commit()

        log_action(f"News {news_id} removed")
        return redirect(url_for("list_news"))

    return manage_delete_item(news_id, "news", drop_news)


def update_news_on_s3():
    # Regenerate event/today.xml on s3 if needed
    if s3:
        event_xml = event_today()
        s3.upload_fileobj(BytesIO(event_xml), config.r2_bucket_name, "event/today.xml")

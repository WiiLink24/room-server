from models import Logs, db
from .admin import oidc
from room import app
from flask import session, render_template, request
import datetime
from theunderground.admin import oidc

def log_action(action: str):
    obj = Logs(
        action=action,
        user=session["oidc_auth_profile"]["nickname"],
        timestamp= datetime.datetime.now()
    )

    db.session.add(obj)
    db.session.commit()


@app.route("/theunderground/logs")
@oidc.require_login
def show_logs():
    page_num = request.args.get("page", default=1, type=int)

    logs = Logs.query.order_by(Logs.timestamp.desc()).paginate(
        page=page_num, per_page=15, error_out=False
    )

    return render_template("list_logs.html", logs=logs, type_length=logs.total)

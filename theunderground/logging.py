from models import Logs, db
from .admin import oidc
from room import app
from flask import session

def log_action(action: str):
    obj = Logs(
        action=action,
        user=session["oidc_auth_profile"]["nickname"]
    )

    db.session.add(obj)
    db.session.commit()
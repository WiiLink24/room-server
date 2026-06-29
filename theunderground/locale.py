from models import Locale
from flask import request, g
from room import app


@app.context_processor
def inject_locales():
    return dict(locales=Locale.choices())


@app.before_request
def set_current_locale():
    if not request.args.get("l"):
        g.current_locale = Locale.En
    else:
        g.current_locale = Locale(request.args.get("l"))


def get_current_locale():
    if "current_locale" not in g:
        # Really should never happen however just to be safe
        return Locale.En

    return g.current_locale

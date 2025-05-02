import uuid
from flask import url_for, flash, render_template, send_from_directory, session
from werkzeug.utils import redirect
from flask_oidc import OpenIDConnect
from first import conf_first_bin_xml
from room import app
import config
import traceback


oidc = OpenIDConnect(app)


@app.context_processor
def inject_oidc():
    return dict(oidc=oidc)


def is_maintenance():
    returned_xml = conf_first_bin_xml()
    if b"<maint>1</maint>" in returned_xml:
        return True
    else:
        return False


@app.route("/")
def index():
    return redirect(url_for("root"))


@app.route("/theunderground")
@app.route("/theunderground/")
def root():
    return redirect(url_for("login"))


@app.route("/theunderground/login")
def login():
    if oidc.user_loggedin:
        return redirect(url_for("admin"))

    return render_template("login.html")


@app.route("/theunderground/logout")
@oidc.require_login
def logout():
    oidc.logout()
    response = redirect(config.oidc_logout_url)
    response.set_cookie("session", expires=0)
    return response


@app.route("/theunderground/admin")
@oidc.require_login
def admin():
    return render_template("underground.html", maintenance=is_maintenance())


# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "errors/error.html",
            error_code=404,
            error_title="Page Not Found",
            error_message="The page you're looking for doesn't exist or has been moved.",
            error_details=str(e),
        ),
        404,
    )


@app.errorhandler(500)
def server_error(e):
    return (
        render_template(
            "errors/error.html",
            error_code=500,
            error_title="Server Error",
            error_message="Something went wrong on our end. Please contact a developer.",
            error_details=str(e),
        ),
        500,
    )


@app.errorhandler(401)
def unauthorized(e):
    return (
        render_template(
            "errors/error.html",
            error_code=401,
            error_title="Unauthorized",
            error_message="You need to be authenticated to access this resource.",
            error_details=str(e),
        ),
        401,
    )


@app.errorhandler(403)
def forbidden(e):
    return (
        render_template(
            "errors/error.html",
            error_code=403,
            error_title="Forbidden",
            error_message="You don't have permission to access this resource.",
            error_details=str(e),
        ),
        403,
    )


@app.errorhandler(Exception)
def handle_exception(e):
    # First check for HTTP exceptions with code attribute
    if hasattr(e, "code"):
        try:
            code = int(e.code)
            if 400 <= code < 600:
                return e
        except (ValueError, TypeError):
            pass

    # Handle authentication errors
    if (
        isinstance(e, str)
        or "MismatchingStateError" in str(e)
        or "invalid_request" in str(e)
    ):
        try:
            session.clear()
        except Exception:
            pass  # In case session is not available

        return (
            render_template(
                "errors/error.html",
                error_code="Auth",
                error_title="Authentication Error",
                error_message="There was a problem with your authentication session. Please try logging in again.",
                error_details=str(e),
                auto_redirect=True,
            ),
            400,
        )

    # Default: handle as general server error
    return (
        render_template(
            "errors/error.html",
            error_code=500,
            error_title="Server Error",
            error_message="An unexpected error occurred.",
            error_details=traceback.format_exc(),
        ),
        500,
    )

from flask import (
    Blueprint,
    redirect,
    url_for,
    session
)

from database.database import get_user

developer = Blueprint("developer", __name__)


# =====================================================
# DEVELOPER DASHBOARD
# =====================================================

@developer.route("/developer-dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("home"))

    user = get_user(session["username"])

    if user[5] != "Project Developer":
        return redirect(url_for("welcome"))

    return "<h1>Developer Dashboard - Coming Soon</h1>"
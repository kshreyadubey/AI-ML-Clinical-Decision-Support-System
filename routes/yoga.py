from flask import (
    Blueprint,
    redirect,
    url_for,
    session
)

from database.database import get_user

yoga = Blueprint("yoga", __name__)


# =====================================================
# YOGA DASHBOARD
# =====================================================

@yoga.route("/yoga-dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("home"))

    user = get_user(session["username"])

    if user[5] != "Yoga Therapist":
        return redirect(url_for("welcome"))

    return "<h1>Yoga Dashboard - Coming Soon</h1>"
from flask import (
    Blueprint,
    redirect,
    url_for,
    session
)

from database.database import get_user

doctor = Blueprint("doctor", __name__)


# =====================================================
# DOCTOR DASHBOARD
# =====================================================

@doctor.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("home"))

    user = get_user(session["username"])

    if user[5] != "Doctor":
        return redirect(url_for("welcome"))

    return "<h1>Doctor Dashboard - Coming Soon</h1>"
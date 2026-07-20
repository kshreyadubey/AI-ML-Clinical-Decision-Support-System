from flask import (
    Blueprint,
    redirect,
    url_for,
    session
)

from database.database import get_user

patient = Blueprint("patient", __name__)


# =====================================================
# PATIENT DASHBOARD
# =====================================================

@patient.route("/patient-dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("home"))

    user = get_user(session["username"])

    if user[5] != "Patient":
        return redirect(url_for("welcome"))

    return "<h1>Patient Dashboard - Coming Soon</h1>"
from flask import (
    Blueprint,
    redirect,
    url_for,
    session
)

from database.database import get_user

acupuncture = Blueprint("acupuncture", __name__)


# =====================================================
# ACUPUNCTURE DASHBOARD
# =====================================================

@acupuncture.route("/acupuncture-dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("home"))

    user = get_user(session["username"])

    if user[5] != "Acupuncture Specialist":
        return redirect(url_for("welcome"))

    return "<h1>Acupuncture Dashboard - Coming Soon</h1>"
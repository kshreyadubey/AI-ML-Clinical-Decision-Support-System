from flask import (
    Blueprint,
    redirect,
    url_for,
    session
)

from database.database import get_user

dietitian = Blueprint("dietitian", __name__)


# =====================================================
# DIETITIAN DASHBOARD
# =====================================================

@dietitian.route("/diet-dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("home"))

    user = get_user(session["username"])

    if user[5] != "Dietitian":
        return redirect(url_for("welcome"))

    return "<h1>Dietitian Dashboard - Coming Soon</h1>"
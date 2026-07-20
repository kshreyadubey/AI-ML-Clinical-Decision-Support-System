from flask import Flask, render_template, redirect, url_for, session

from database.database import (
    create_database,
    insert_default_users,
    get_user
)

# =====================================================
# IMPORT BLUEPRINTS
# =====================================================

from routes.auth import auth
from routes.doctor import doctor
from routes.patient import patient
from routes.dietitian import dietitian
from routes.yoga import yoga
from routes.acupuncture import acupuncture
from routes.developer import developer

app = Flask(__name__)

app.secret_key = "ArogyaAI_2026_SECRET_KEY"

# =====================================================
# REGISTER BLUEPRINTS
# =====================================================

app.register_blueprint(auth)
app.register_blueprint(doctor)
app.register_blueprint(patient)
app.register_blueprint(dietitian)
app.register_blueprint(yoga)
app.register_blueprint(acupuncture)
app.register_blueprint(developer)

# =====================================================
# INITIALIZE DATABASE
# =====================================================

create_database()
insert_default_users()


# =====================================================
# HOME PAGE
# =====================================================

@app.route("/")
def home():

    return render_template("login.html")


# =====================================================
# SUCCESS PAGE
# =====================================================

@app.route("/success")
def success():

    return render_template("success.html")


# =====================================================
# WELCOME PAGE
# =====================================================

@app.route("/welcome")
def welcome():

    if "username" not in session:
        return redirect(url_for("home"))

    user = get_user(session["username"])

    return render_template(
        "welcome.html",
        username=user[1],
        fullname=user[3],
        role=user[5]
    )


# =====================================================
# START APPLICATION
# =====================================================

@app.route("/start-application")
def start_application():

    if "username" not in session:
        return redirect(url_for("home"))

    user = get_user(session["username"])
    role = user[5]

    if role == "Doctor":
        return redirect(url_for("doctor.dashboard"))

    elif role == "Patient":
        return redirect(url_for("patient.dashboard"))

    elif role == "Dietitian":
        return redirect(url_for("dietitian.dashboard"))

    elif role == "Yoga Therapist":
        return redirect(url_for("yoga.dashboard"))

    elif role == "Acupuncture Specialist":
        return redirect(url_for("acupuncture.dashboard"))

    elif role == "Project Developer":
        return redirect(url_for("developer.dashboard"))

    return redirect(url_for("home"))


# =====================================================
# RUN APPLICATION
# =====================================================

if __name__ == "__main__":

    app.run(debug=True)
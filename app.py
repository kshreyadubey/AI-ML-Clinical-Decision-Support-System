from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ======================================================
# OFFICIAL USERS
# ======================================================

USERS = {

    "dr_srikant": {
        "password": "Doctor@2026",
        "role": "Doctor"
    },

    "deepika": {
        "password": "Yoga@2026",
        "role": "Yoga Therapist"
    },

    "diet01": {
        "password": "Diet@2026",
        "role": "Dietitian"
    },

    "acu01": {
        "password": "Acu@2026",
        "role": "Acupuncture"
    },

    "patient01": {
        "password": "Patient@2026",
        "role": "Patient"
    },

    "shreya": {
        "password": "Shreya@2026",
        "role": "Developer"
    }

}

# ======================================================
# TEMP ACTIVATED USERS
# ======================================================

ACTIVATED_USERS = [

    "shreya"

]

# ======================================================
# LOGIN PAGE
# ======================================================

@app.route("/")
def home():

    return render_template("login.html")


# ======================================================
# LOGIN
# ======================================================

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username not in USERS:

        return render_template(
            "login.html",
            error="Invalid Username."
        )

    if USERS[username]["password"] != password:

        return render_template(
            "login.html",
            error="Invalid Password."
        )

    if username not in ACTIVATED_USERS:

        return render_template(
            "login.html",
            error="Account not registered. Please register first."
        )

    return redirect("/dashboard")


# ======================================================
# VERIFY PAGE
# ======================================================

@app.route("/verify")
def verify():

    return render_template("verify.html")


# ======================================================
# VERIFY CREDENTIALS
# ======================================================

@app.route("/verify", methods=["POST"])
def verify_user():

    username = request.form["username"]
    password = request.form["password"]

    if username in USERS and USERS[username]["password"] == password:

        return redirect("/register")

    return render_template(
        "verify.html",
        error="Invalid Official Username or Password."
    )


# ======================================================
# REGISTER PAGE
# ======================================================

@app.route("/register")
def register():

    return render_template("register.html")


# ======================================================
# REGISTER FORM
# ======================================================

@app.route("/register", methods=["POST"])
def register_user():

    fullname = request.form["fullname"]
    mobile = request.form["mobile"]
    otp = request.form["otp"]

    # Tomorrow
    # SQLite
    # Twilio
    # Activation

    return redirect("/success")


# ======================================================
# SUCCESS PAGE
# ======================================================

@app.route("/success")
def success():

    return render_template("success.html")


# ======================================================
# DASHBOARD
# ======================================================

@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")


# ======================================================
# RUN
# ======================================================

if __name__ == "__main__":

    app.run(debug=True)
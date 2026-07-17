from flask import Flask, render_template, request, redirect, url_for, session

from database.database import (
    create_database,
    insert_default_users,
    check_login,
    is_registered,
    register_user,
    get_user
)

from services.otp_service import (
    send_otp,
    verify_otp
)

app = Flask(__name__)

app.secret_key = "ArogyaAI_2026_SECRET_KEY"

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
# LOGIN
# =====================================================

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"].strip()
    password = request.form["password"].strip()

    user = check_login(username, password)

    if not user:

        return render_template(
            "login.html",
            error="Invalid Username or Password."
        )

    if not is_registered(username):

        return render_template(
            "login.html",
            error="Account not registered. Please register first."
        )

    session["username"] = username

    return redirect(url_for("welcome"))


# =====================================================
# VERIFY PAGE
# =====================================================

@app.route("/verify")
def verify():

    return render_template("verify.html")


# =====================================================
# VERIFY OFFICIAL CREDENTIALS
# =====================================================

@app.route("/verify", methods=["POST"])
def verify_user():

    username = request.form["username"].strip()
    password = request.form["password"].strip()

    user = check_login(username, password)

    if not user:

        return render_template(
            "verify.html",
            error="Invalid Official Username or Password."
        )

    if is_registered(username):

        return render_template(
            "verify.html",
            error="This account is already registered. Please login."
        )

    session["register_username"] = username

    return redirect(url_for("register"))


# =====================================================
# REGISTER PAGE
# =====================================================

@app.route("/register")
def register():

    if "register_username" not in session:

        return redirect(url_for("verify"))

    return render_template("register.html")
@app.route("/send-otp", methods=["POST"])
def send_registration_otp():

    if "register_username" not in session:
        return redirect(url_for("verify"))

    fullname = request.form["fullname"].strip()
    mobile = request.form["mobile"].strip()

    if len(mobile) != 10 or not mobile.isdigit():

        return render_template(
            "register.html",
            error="Please enter a valid 10-digit mobile number."
        )

    session["fullname"] = fullname
    session["mobile"] = mobile

    phone = "+91" + mobile

    try:

        send_otp(phone)

        return render_template(
            "register.html",
            success="OTP sent successfully.",
            fullname=fullname,
            mobile=mobile,
            otp_sent=True
        )

    except Exception as e:

        return render_template(
            "register.html",
            error=str(e),
            fullname=fullname,
            mobile=mobile
        )


# =====================================================
# COMPLETE REGISTRATION
# =====================================================

@app.route("/register", methods=["POST"])
def complete_registration():

    if "register_username" not in session:
        return redirect(url_for("verify"))

    username = session["register_username"]

    fullname = request.form["fullname"].strip()
    mobile = request.form["mobile"].strip()
    otp = request.form["otp"].strip()

    phone = "+91" + mobile

    try:

        verified = verify_otp(phone, otp)

        if not verified:

            return render_template(
                "register.html",
                error="Incorrect OTP. Please try again.",
                fullname=fullname,
                mobile=mobile,
                otp_sent=True
            )

        register_user(
            username,
            fullname,
            mobile
        )

        session.pop("register_username", None)
        session.pop("fullname", None)
        session.pop("mobile", None)

        return redirect(url_for("success"))

    except Exception as e:

        return render_template(
            "register.html",
            error=str(e),
            fullname=fullname,
            mobile=mobile,
            otp_sent=True
        )


# =====================================================
# SUCCESS PAGE
# =====================================================

@app.route("/success")
def success():

    return render_template("success.html")


# =====================================================
# DASHBOARD
# =====================================================

@app.route("/dashboard")
def dashboard():

    if "username" not in session:

        return redirect(url_for("home"))

    user = get_user(session["username"])

    return render_template(
        "dashboard.html",
        username=user[1],
        fullname=user[3],
        role=user[5]
    )
# =====================================================
# PATIENT DASHBOARD
# =====================================================

@app.route("/patient-dashboard")
def patient_dashboard():

    return "<h1>Patient Dashboard - Coming Soon</h1>"


# =====================================================
# DIET DASHBOARD
# =====================================================

@app.route("/diet-dashboard")
def diet_dashboard():

    return "<h1>Dietitian Dashboard - Coming Soon</h1>"


# =====================================================
# YOGA DASHBOARD
# =====================================================

@app.route("/yoga-dashboard")
def yoga_dashboard():

    return "<h1>Yoga Dashboard - Coming Soon</h1>"


# =====================================================
# ACUPUNCTURE DASHBOARD
# =====================================================

@app.route("/acupuncture-dashboard")
def acupuncture_dashboard():

    return "<h1>Acupuncture Dashboard - Coming Soon</h1>"


# =====================================================
# DEVELOPER DASHBOARD
# =====================================================

@app.route("/developer-dashboard")
def developer_dashboard():

    return "<h1>Developer Dashboard - Coming Soon</h1>"
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

        return redirect(url_for("dashboard"))

    elif role == "Patient":

        return redirect(url_for("patient_dashboard"))

    elif role == "Dietitian":

        return redirect(url_for("diet_dashboard"))

    elif role == "Yoga Therapist":

        return redirect(url_for("yoga_dashboard"))

    elif role == "Acupuncture Specialist":

        return redirect(url_for("acupuncture_dashboard"))

    elif role == "Project Developer":

        return redirect(url_for("developer_dashboard"))

    return redirect(url_for("dashboard"))


# =====================================================
# LOGOUT
# =====================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# =====================================================
# RUN APPLICATION
# =====================================================

if __name__ == "__main__":

    app.run(debug=True)
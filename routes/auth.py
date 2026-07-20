from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from database.database import (
    check_login,
    is_registered,
    register_user
)

from services.otp_service import (
    send_otp,
    verify_otp
)

auth = Blueprint("auth", __name__)


# =====================================================
# LOGIN
# =====================================================

@auth.route("/login", methods=["POST"])
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

@auth.route("/verify")
def verify():

    return render_template("verify.html")


# =====================================================
# VERIFY OFFICIAL CREDENTIALS
# =====================================================

@auth.route("/verify", methods=["POST"])
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

    return redirect(url_for("auth.register"))


# =====================================================
# REGISTER PAGE
# =====================================================

@auth.route("/register")
def register():

    if "register_username" not in session:

        return redirect(url_for("auth.verify"))

    return render_template("register.html")


# =====================================================
# SEND OTP
# =====================================================

@auth.route("/send-otp", methods=["POST"])
def send_registration_otp():

    if "register_username" not in session:
        return redirect(url_for("auth.verify"))

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

@auth.route("/register", methods=["POST"])
def complete_registration():

    if "register_username" not in session:
        return redirect(url_for("auth.verify"))

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
# LOGOUT
# =====================================================

@auth.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))
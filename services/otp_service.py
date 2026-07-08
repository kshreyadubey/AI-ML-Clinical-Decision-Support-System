from twilio.rest import Client
from config.config import ACCOUNT_SID, AUTH_TOKEN, VERIFY_SERVICE_SID


client = Client(ACCOUNT_SID, AUTH_TOKEN)


# ==========================================
# SEND OTP
# ==========================================

def send_otp(phone_number):

    verification = client.verify.v2.services(
        VERIFY_SERVICE_SID
    ).verifications.create(
        to=phone_number,
        channel="sms"
    )

    return verification.status


# ==========================================
# VERIFY OTP
# ==========================================

def verify_otp(phone_number, otp):

    verification_check = client.verify.v2.services(
        VERIFY_SERVICE_SID
    ).verification_checks.create(
        to=phone_number,
        code=otp
    )

    return verification_check.status == "approved"
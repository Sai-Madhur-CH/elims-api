from flask import current_app as app, jsonify, make_response, render_template
from db.connection import db
from models.app_users import AppUsers
from utils.email_util import EmailUtil
from services.login_service import generate_hased_password
import string
import random

def otp_email_send(data):
    """
    To generate a OTP based on the details provided by the user and if the user email and phone matches 
    generate a email which contails the OTP.
    """
    user = AppUsers().get_user(data)
    if user:
        password = generate_otp(user)
        client = EmailUtil()
        user = { **user, **{'password':password,'link':app.config['WEB_SITE_LINK']}}
        msg = client.message(render_template('forgot_password.html', user=user), 'Recovery OTP', [user.get('email')], [], msg_type="html")
        client.send_mail(msg, [user.get('email')])
        return make_response(jsonify({'status':'success'}), 200)
    return make_response(jsonify({'status':'unauthorized user'}), 200)

def generate_otp(user):
    password = random_password()
    user['hashed_password'] = str(generate_hased_password(password))
    user['login_count'] = 0
    user['login_attempts'] = 0
    AppUsers().update_app_user(user)
    return password

def random_password():
    return ''.join(random.sample(string.ascii_letters+string.digits,8))


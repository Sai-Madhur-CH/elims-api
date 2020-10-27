from flask import current_app as app, jsonify, make_response
from db.connection import db
from models.app_users import AppUsers
from services.login_service import generate_hased_password

def update_user_password(data, app_user):
    """
    To get the user form the token and changing the password based on input given by user
    """
    app_user['hashed_password'] = str(generate_hased_password(data.get('confirm_password')))
    AppUsers().update_app_user(app_user)
    return make_response(jsonify({'status':'success'}),200)
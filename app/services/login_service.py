from flask import current_app as app, jsonify, make_response
from db.connection import db
from models.app_users import AppUsers
import jwt
import bcrypt
import ast
import datetime


key = 'vadajdvcsad vzsfcgawsfdcusat gcvnazsdjhfcgusadvc'

def login(data):
    """
    To authentic the username / phone number and password provide by the user and if its a match
    generate a JWT token lasting for 1 hour.
    """

    user = AppUsers().get_user({'email': data['email_phone']})
    if user is None:
        user = AppUsers().get_user({'phone': data['email_phone']})

    if user:
        if bcrypt.checkpw(data['password'].encode('utf-8'),ast.literal_eval(user.get('hashed_password'))):
            user['token'] = generate_token(user).decode('utf-8')
            user.pop('hashed_password',None)
            return make_response(jsonify(user),200)
    else:
        return make_response(jsonify({'status':'unauthorized user'}),401)

def register_user(data):
    """
    To create a Super Admin
    """

    AppUsers(
        name=data.get('name'),
        role_id=data.get('role_id'),
        email=data.get('email'),
        phone=data.get('phone'),
        hashed_password=str(generate_hased_password(data.get('password'))),
        status='active'
    ).save()

    return jsonify({'status':'success'})


def generate_hased_password(password):
    salt_value = bcrypt.gensalt(9)
    return bcrypt.hashpw(password.encode('utf-8'), salt_value)

def generate_token(user):
    token=jwt.encode({
        'name':user.get('name'),
        'user_id':user.get('user_id'),
        'role_id':user.get('role_id'),
        'role_name':user.get('role_name'),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        },key)
    return token
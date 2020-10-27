from flask import current_app as app, jsonify, make_response, request
from db.connection import db
from models.app_users import AppUsers
import jwt
import bcrypt
import ast
import datetime
from dateutil.relativedelta import relativedelta
from functools import wraps

key = 'vadajdvcsad vzsfcgawsfdcusat gcvnazsdjhfcgusadvc'

def login(data):
    """
    To authentic the username / phone number and password provide by the user and if its a match
    generate a JWT token lasting for 1 hour.
    """
    check = False
    user = AppUsers().get_user({'email': data.get('email_phone')})
    if user is None:
        user = AppUsers().get_user({'phone': data.get('email_phone')})

    if user:

        if bcrypt.checkpw(data['password'].encode('utf-8'),ast.literal_eval(user.get('hashed_password'))) and check_status(user):
            check = True
            user['token'] = generate_token(user).decode('utf-8')
            user.pop('hashed_password',None)
            user['login_count'] = int(user['login_count'] or 0) + 1
            user['login_attempts'] = 0
            user['last_login_date'] = datetime.datetime.now()
            AppUsers.update_app_user(user)
            return make_response(jsonify(user),200)

        elif check == False and user['login_attempts'] <= 2:
            user['login_attempts'] = int(user['login_attempts'] or 0) + 1
            AppUsers.update_app_user(user)
            msg = 'Wrong password, remaining login attempts {0}'.format(str( 3 - int(user['login_attempts'] or 0) ))
            return make_response(jsonify({'status':'wrong password','msg': msg}),200)

        elif user['login_attempts'] > 2:
            user['status'] = 'inactive'
            user['last_login_date'] = datetime.datetime.now()
            AppUsers.update_app_user(user)
            return make_response(jsonify({'status':'inactive'}),200)

    else:
        return make_response(jsonify({'status':'unauthorized user'}),200)


def check_status(user):
    if user.get('status') == 'active':
        return True
    elif (user.get('status') == 'inactive' and user.get('login_attempts') >= 3 and
        datetime.datetime.now() < user.get('last_login_date') + relativedelta(hours=24)):
        return False
    return False

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

def jwt_required(func):
    @wraps(func)
    def login_required(*args, **kwargs):

        jwt_token=request.headers.get('Authorization',None)

        if jwt_token:

            try:
                decode=jwt.decode(jwt_token,key)
            except:
                return {'status':'Invalid Token'}

            result=AppUsers().get_user({'user_id':decode.get('user_id')})

            if result !=None:
                kwargs['app_user'] = result
                return func(*args, **kwargs)

        return {'message':'Enter the Authorization token in Headers'}

    return login_required
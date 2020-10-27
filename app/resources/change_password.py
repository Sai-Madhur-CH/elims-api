from flask import current_app as app, jsonify, request, make_response
import jwt
from flask_restful import Resource
import services.change_password_service as cp
from services.login_service import jwt_required

class ChangePassword(Resource):
    """
    To update the auto generated password to the user wanted password when they first try to login.
    """
    def __init__(self):
        self.error_msg = 'please provide valid data'

    @jwt_required
    def put(self, app_user):
        data = request.get_json()
        if isinstance(data, dict):
            return cp.update_user_password(data, app_user)
        return make_response(jsonify({'status':self.error_msg}),200)

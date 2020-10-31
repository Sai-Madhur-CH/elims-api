from flask import current_app as app, jsonify, request, make_response
import jwt
from flask_restful import Resource
import services.forgot_password_service as fp

class ForgotPassword(Resource):
    def __init__(self):
        self.error_msg = 'please provide valid data'

    def post(self):
        data = request.get_json()
        if isinstance(data, dict):
            data.pop('method', None)
            return fp.otp_email_send(data)
        return make_response(jsonify({'status':self.error_msg}),200)
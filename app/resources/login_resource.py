from flask import current_app as app, jsonify, request
from flask_restful import Resource
from models.app_users import AppUsers
import services.login_service as ls


class Login(Resource):
    """
    Login Resource
    """

    def __init__(self):
        self.error_msg = 'please provide valid data'


    def post(self):
        data = request.get_json()
        if isinstance(data, dict):
            return ls.login(data)
        return jsonify({'status':self.error_msg}),500
           

    def put(self):
        data = request.get_json()
        if isinstance(data, dict):
            return ls.register_user(data)
        return jsonify({'status':self.error_msg}),500

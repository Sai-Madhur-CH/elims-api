from flask import current_app as app, jsonify
from flask_restful import Resource
from models.app_users import AppUsers


class Login(Resource):
    """
    Login Resource
    """

    def get(self):
        users = AppUsers().get_app_users()
        return jsonify({'users':users,'status':'success'})

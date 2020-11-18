from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from db.connection import db
import os

app = Flask(__name__)
api = Api(app)
CORS(app)

db.init_app(app)

app.config.from_pyfile(os.path.join(os.getcwd(), 'conf',
                                    '{0}.py'.format(os.getenv('NODE_ENV', 'conf').lower())))

with app.app_context():
    from resources.login_resource import Login
    from resources.change_password import ChangePassword
    from resources.forgot_password import ForgotPassword
    from resources.lab_catalog import LabList, LabTestList

    api.add_resource(Login, '/login')
    api.add_resource(ChangePassword, '/change_password')
    api.add_resource(ForgotPassword, '/forgot_password')
    api.add_resource(LabList, '/labs')
    api.add_resource(LabTestList, '/lab_tests')


if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'], 
            debug=app.config['DEBUG'])

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
    api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'], debug=app.config['DEBUG'])

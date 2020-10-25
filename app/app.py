from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from db.connection import db
import os

app = Flask(__name__)
api = Api(app)
CORS(app)

db.init_app(app)

app.config.from_pyfile(os.path.join(os.getcwd(), 'config', '{0}.py'.format(os.getenv('NODE_ENV', 'conf').lower())))

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])

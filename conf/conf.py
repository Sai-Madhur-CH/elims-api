# DB Connections
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@127.0.01:5430/ECLIMS'
SQLALCHEMY_TRACK_MODIFICATIONS = True
PROPAGATE_EXCEPTIONS = True
# Application Config
HOST = '127.0.0.1'
PORT = 8001
DEBUG = True
# SMTP Config
SMTP_SERVER = 'mail.eisbiz.net'
SMTP_PORT = 465
EMAIL_ID = 'noreply-eclims@eisbiz.net'
PASSWORD = 'Eisbiz@2020'
WEB_SITE_LINK = 'http:/localhost:3000/'
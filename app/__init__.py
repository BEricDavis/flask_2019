from flask import Flask
# Extensions get added to this file

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import logging
from logging.handlers import SMTPHandler
# "app" here is an instance of the Flask class.
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                      fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                      toaddrs=app.config['ADMINS'],
                      subject='Microblog Failure',
                      credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        # Flask's logger is already defined by default
        app.logger.addHandler(mail_handler)


# "app" here is the app packags
# this line goes at the very bottom of the file
from app import routes, models, errors
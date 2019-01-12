from flask import Flask
# Extensions get added to this file
# the import of Config works though pycharm complains it can't resolve it
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# "app" here is an instance of the Flask class.
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
# "app" here is the app packags; thiis works though PyCharm complains
from app import routes, models, errors
from flask import Flask
# the import of Config works though pycharm complains it can't resolve it
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# "app" here is an instance of the Flask class.
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# "app" here is the app packags; thiis works though PyCharm complains
from app import routes, models
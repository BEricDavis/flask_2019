from flask import Flask
# the import of Config works though pycharm complains it can't resolve it
from config import Config

# "app" here is an instance of the Flask class.
app = Flask(__name__)
app.config.from_object(Config)

# "app" here is the app packags; thiis works though PyCharm complains
from app import routes
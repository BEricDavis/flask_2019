from flask import Flask

# "app" here is an instance of the Flask class.
app = Flask(__name__)

# "app" here is the app packags
from app import routes
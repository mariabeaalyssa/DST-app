from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin

server = Flask(__name__)
dbase = SQLAlchemy(server)

server.config['SECRET_KEY'] = 'secretsecretsecret'
server.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kezivpkchqtuqm:a2f4dd544c4b42e06bebce8d88b04a3c925d4f847f4282119608e930e14654c7@ec2-3-209-39-2.compute-1.amazonaws.com:5432/dfu124ghuikg3a'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(server)

from app.models import *
from app.forms import *
from app.routes import *

dbase.create_all()
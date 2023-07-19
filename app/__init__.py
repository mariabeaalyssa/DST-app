from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin

server = Flask(__name__)
dbase = SQLAlchemy(server)

server.config['SECRET_KEY'] = 'secretsecretsecret'
server.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xsaiqclfnizczq:dd6b7692e7aa6df613efcfd60a7e99015a538c66bf04eccc65e256df360943a4@ec2-3-93-206-109.compute-1.amazonaws.com:5432/dglg9dmo4mf71'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(server)

from app.models import *
from app.forms import *
from app.routes import *

dbase.create_all()
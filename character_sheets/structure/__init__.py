from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'char4cterhar4ct0r'

db = SQLAlchemy
bcrypt = Bcrypt(app)
login_manager = Loginmanager(app)
login_manager.login_view = 'login'

from '' import route
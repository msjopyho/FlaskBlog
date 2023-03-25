import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager

app = Flask(__name__)

conn = sqlite3.connect('flaskblog/site.db')  # create and connect a database file

app.config['SECRET_KEY'] = 'a;sdfioh;2i3h-123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes

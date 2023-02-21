import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

conn = sqlite3.connect('flaskblog/site.db')  # create and connect a database file

app.config['SECRET_KEY'] = 'a;sdfioh;2i3h-123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
#from task import app
#from task import db
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "shhhhh"

db = SQLAlchemy(app)

from application import routes
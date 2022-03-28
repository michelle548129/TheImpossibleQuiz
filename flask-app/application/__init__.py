from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
import pymysql
from os import getenv
from flask_wtf import FlaskForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('db_uri') #"mysql+pymysql://root:Pluto100@35.189.93.155:3306/flask_demo_db"
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = "this is my secret key"

db = SQLAlchemy(app)

from application import routes, forms, models
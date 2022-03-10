from flask import Flask
from application import app
from flask import request
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange
from datetime import date

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')


db = SQLAlchemy(app)
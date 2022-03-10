from flask import Flask
from application import app
from flask import request
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange, DataRequired
from datetime import date

class AddItem(FlaskForm):
    item_name = StringField('Item name', validators=[DataRequired(message="This field cannot be left blank")])
    price = IntegerField("Price", validators=[DataRequired(message="This field cannot be left blank")])
    description = StringField("Item Description", validators=[DataRequired(message="This field cannot be left blank")])
    quantity = IntegerField("Quantity", validators=[DataRequired(message="This field cannot be left blank")])
    submit = SubmitField("Add Item")

class UpdateItem(FlaskForm):
    item_name = StringField('Item name', validators=[DataRequired(message="This field cannot be left blank")])
    price = IntegerField("Price", validators=[DataRequired(message="This field cannot be left blank")])
    description = StringField("Item Description", validators=[DataRequired(message="This field cannot be left blank")])
    quantity = IntegerField("Quantity", validators=[DataRequired(message="This field cannot be left blank")])
    submit = SubmitField("Update Item")

class ChooseItem(FlaskForm):
    chosenItem = SelectField('Item', choices=[])
    submit = SubmitField("Choose Item")
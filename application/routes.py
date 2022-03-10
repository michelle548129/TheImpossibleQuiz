from flask import redirect, url_for, render_template, request
from application import app, db
from datetime import date, timedelta
from application.models import user, purchase, item
from application.forms import AddItem, UpdateItem, ChooseItem

@app.route('/home', methods=["GET", "POST"])
@app.route('/', methods=["GET", "POST"])
def home():
   if request.form:
      print(request.form)
   return render_template('home.html')


@app.route('/basket', methods=["GET", "POST"])
def basket():
   if request.form:
      print(request.form)
   return render_template('basket.html')


@app.route('/admin_page', methods=["GET", "POST"])
def admin_page():
   form = AddItem()
   if request.method == 'POST':
      item_name = form.item_name.data
      price = form.price.data
      description = form.description.data
      newItem = item(item_name = item_name, price=price, description = description)
      db.session.add(newItem)
      db.session.commit()
   return render_template('admin_page.html')





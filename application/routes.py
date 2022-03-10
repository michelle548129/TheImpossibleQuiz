from flask import redirect, url_for, render_template, request
from application import app, db
from datetime import date, timedelta
from application.models import user, purchase, item

@app.route('/home', methods=["GET", "POST"])
@app.route('/', methods=["GET", "POST"])
def home():
   if request.form:
      i = item(item_name=request.form.get("Item Name"))
      db.session.add(i)
      db.session.commit()
   return render_template('home.html')


@app.route('/shop', methods=["GET", "POST"])
def shop():
   if request.form:
      item = Item(item_name=request.form.get("Item Name"))
      db.session.add(item)
      db.session.commit()
   return render_template('shop.html')

@app.route('/basket', methods=["GET", "POST"])
def basket():
   if request.form:
      print(request.form)
   return render_template('basket.html')



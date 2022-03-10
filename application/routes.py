from flask import redirect, url_for, render_template, request
from application import app, db
from datetime import date, timedelta
from application.models import user, purchase, item
from application.forms import AddItem, UpdateItem, ChooseItem

@app.route('/home', methods=["GET", "POST"])
@app.route('/', methods=["GET", "POST"])
def home():
   allItems = item.query.all()
   return render_template("home.html", allItems=allItems)
  


@app.route('/basket', methods=["GET", "POST"])
def basket():
   if request.form:
      print(request.form)
   return render_template('basket.html')


@app.route('/admin_page', methods=["GET", "POST"])
def admin_page():
   form = AddItem()
   allItems = item.query.all()
   if request.method == 'POST':
      item_name = form.item_name.data
      price = form.price.data
      description = form.description.data
      quantity = form.quantity.data
      newItem = item(item_name = item_name, price=price, description = description, quantity = quantity)
      db.session.add(newItem)
      db.session.commit()
   return render_template('admin_page.html', allItems=allItems)


@app.route("/update_quantity", methods=["POST"])
def update_quantity():
    newquantity = request.form.get("newquantity")
    oldquantity = request.form.get("oldquantity")
    finalQuantity = item.query.filter_by(quantity=oldquantity).first()
    finalQuantity.quantity = newquantity
    db.session.commit()
    return redirect("/")




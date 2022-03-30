from flask import redirect, url_for, render_template, request
from application import app, db
from datetime import date, timedelta
from application.models import user, purchase, item
from application.forms import AddItem, UpdateItem, ChooseItem, AddUser, CreateRequest

@app.route('/home', methods=["GET", "POST"])
@app.route('/', methods=["GET", "POST"])
def home():
  # allItems = item.query.all()
   return render_template("home.html", allItems=allItems)
  

@app.route('/user_page', methods=["GET", "POST"])
def user_page():
   form = AddUser()
   if request.method == 'POST':
      user_name = form.user_name.data
      email = form.email.data
      address = form.address.data
      newUser = user(user_name = user_name, email=email, address = address)
      db.session.add(newUser)
      db.session.commit()
   return render_template('user_page.html')


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
   
@app.route("/purchase", methods=["POST"])
def purchase():
   if request.form:
      print(request.form)
   return render_template('purchase.html')

   
@app.route("/delete_item", methods=["POST"])
def delete_item():
    item_name = request.form.get("item_name")
    Item = item.query.filter_by(item_name=item_name).first()
    db.session.delete(Item)
    db.session.commit()
    return redirect("/")


@app.route('/basket', methods=['GET', 'POST'])
def basket():
    User = user.query.all()
    Item = item.query.all()
    form = CreateRequest()
    form.user_name.choices.extend([(User.id, str(User)) for User in User])
    form.item_name.choices.extend([(Item.id, str(Item)) for Item in Item])
    if request.method == "POST":
        User = form.user_name.data
        Item = form.item_name.data
        new_request = purchase(fk_user_id=user, fk_item_id=item)
        db.session.add(new_request)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('basket.html', form=form, pageTitle="Create Request")


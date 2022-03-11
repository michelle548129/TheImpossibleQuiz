from application import db
from sqlalchemy.orm import relationship

class purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    fk_item_id = db.Column(db.Integer, db.ForeignKey('item.id'))


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    address = db.Column(db.String(255))
    purchases = db.relationship('purchase', backref='user',
                            lazy='dynamic')
    def __repr__(self):
        return f"{self.user_name}" 


class item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(255))
    price = db.Column(db.Numeric(5,2))
    description = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    def __repr__(self):
        return f"{self.item_name}"    




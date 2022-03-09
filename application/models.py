from application import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))
    user_password = db.Column(db.String(100))
    student = db.Column(db.Boolean)
    teacher = db.Column(db.Boolean)
from app.extensions import db


class RestaurantNum(db.Model):
    __tablename__ = "restaurant_num"
    id = db.Column(db.Integer,primary_key=True)
    city = db.Column(db.String(25))
    area = db.Column(db.String(25))
    number = db.Column(db.Integer)
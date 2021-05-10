from app.extensions import db


class RestaurantTypeCount(db.Model):
    __tablename__ = "restaurant_type_count"
    city = db.Column(db.String(25))
    foodtype = db.Column(db.String(25))
    number = db.Column(db.Integer)
    id = db.Column(db.Integer,primary_key=True)
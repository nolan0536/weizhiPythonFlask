from app.extensions import db

class CityRestaurantNum(db.Model):
    __tablename__ = "city_restaurant_num"
    id = db.Column(db.Integer,primary_key=True)
    city = db.Column(db.String(25))
    restaurant_numb = db.Column(db.Integer)
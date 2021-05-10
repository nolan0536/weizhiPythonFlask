from app.extensions import db


class CitySaleVol(db.Model):
    __tablename__ = "city_sale_vol"
    id = db.Column(db.Integer,primary_key = True)
    city = db.Column(db.String(25))
    area = db.Column(db.String(25))
    sales_vol_month = db.Column(db.Integer)
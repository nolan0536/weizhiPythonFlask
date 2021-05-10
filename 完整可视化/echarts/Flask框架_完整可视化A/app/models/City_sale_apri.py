from app.extensions import db

class CitySaleApri(db.Model):
    __tablename__ = "city_sale_apri"
    city = db.Column(db.String(25))
    area = db.Column(db.String(25))
    sales_month = db.Column(db.Float)
    id = db.Column(db.Integer,primary_key=True)
from app.extensions import db


class RestaurantScoreNum(db.Model):
    __tablename__ = "restaurant_score_num"
    id = db.Column(db.Integer,primary_key=True)
    scoreInterval = db.Column(db.String(25))
    number = db.Column(db.Integer)
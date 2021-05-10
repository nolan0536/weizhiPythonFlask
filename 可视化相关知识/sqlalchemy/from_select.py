from flask import Flask
from sqlalchemy import asc,desc
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
class Config(object):
    user = "root"
    password = "123456"
    dataName = "test"
    # 自动提交配置
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 数据库链接
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@localhost:3306/%s"%(user,password,dataName)
    # 密钥
    SECRET_KEY = "6658AG"

# 初始化配置
app.config.from_object(Config)
# 创建SQLALlchemy对象
db = SQLAlchemy(app)

class Authors(db.Model):
    __tablename__ = "authors"
    aid = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

class Books(db.Model):
    __tablename__ = "books"
    bid = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    author_id = db.Column(db.Integer)

class Marttype_copy(db.Model):
    __tablename__ = "marttype_copy"
    id = db.Column(db.Integer,primary_key = True)
    type = db.Column(db.String(255))
    sale = db.Column(db.Float)
    cost = db.Column(db.Float)
    rate = db.Column(db.Float)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    sex = db.Column(db.String(6))
    age = db.Column(db.Integer)
    password = db.Column(db.String(25))

class Wether2(db.Model):
    __tablename__ = "wether2"
    day = db.Column(db.DateTime,primary_key = True)
    AQI = db.Column(db.Integer)
    lever = db.Column(db.String(255))
    PM2 = db.Column(db.Integer)
    PM10 = db.Column(db.Integer)
    SO2 = db.Column(db.Integer)
    CO = db.Column(db.Integer)
    NO2 = db.Column(db.Integer)
    O3 = db.Column(db.Integer)

# 通配符查询
tmp1 = db.session.query(Marttype_copy).filter(Marttype_copy.type.like("S%")).all()
print(tmp1)
for r in tmp1:
    print(r.id,r.type,r.sale)

print("=========================")
# 多条件查询
tmp2 = db.session.query(Marttype_copy).filter(Marttype_copy.sale>10000,Marttype_copy.cost>6000).all()
for r in tmp2:
    print(r.id,r.sale,r.cost)

print("========================")
# 选择列查询
tmp3 = db.session.query(Books.title).all()
for r in tmp3:
    print(r.title)

print("========================")
# 多表关联查询
tmp4 = db.session.query(Authors,Books).join(Books,Books.author_id==Authors.aid).all()
for r in tmp4:
    print(r[0].name,r[1].title)

print("=========================")
# 分组查询
tmp5 = db.session.query(
    Wether2.day,
    func.sum(Wether2.lever).label("Sum_lever"),
    func.min(Wether2.AQI).label("Min_AQI"),
    func.max(Wether2.PM2).label("Max_PM2"),
    func.avg(Wether2.PM10).label("Avg_PM10")
    ).group_by(Wether2.lever).all()
for r in tmp5:
    print(r.day,r.Sum_lever,r.Min_AQI,r.Max_PM2,r.Avg_PM10)
print("=========================")
# 排序查询
tmp6 = db.session.query(User).order_by(User.age.desc()).all()
for r in tmp6:
    print(r.name,r.age,r.password)
print("==========================")
tmp7 = User.query.order_by(asc("age")).all()
for r in tmp7:
    print(r.age)
print("===========================")
tmp8 = db.session.query(Wether2.day).filter(Wether2.SO2<10,Wether2.lever == "良").order_by(Wether2.day.desc()).all()
for r in tmp8:
    print(r.day)

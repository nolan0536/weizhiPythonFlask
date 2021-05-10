from flask import Flask
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import *


app = Flask(__name__)

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/mart?charset=utf8")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Regionsale(Base):
    __tablename__ = "regionsale"
    id = Column(Integer,primary_key=True)
    province = Column(String(25))
    sale = Column(Integer)

class Monthlysale(Base):
    __tablename__ = "monthlysale"
    id = Column(Integer,primary_key=True)
    year = Column(String(10))
    month = Column(String(20))
    sale = Column(Float)
    cost = Column(Float)

class Marttype(Base):
    __tablename__ = "marttype"
    id = Column(Integer,primary_key=True)
    type = Column(String(155))
    sale = Column(Float)
    cost = Column(Float)

# 通配符查询
tmp1 = session.query(Regionsale).filter(Regionsale.province.like("%A")).all()
for r1 in tmp1:
    print(r1.province,r1.sale)
print("")
# 多条件查询
tmp2 = session.query(Marttype).filter(Marttype.type=="Supermarket",Marttype.cost<4100).all()
for r2 in tmp2:
    print(r2.id,r2.type,r2.cost)
print("")
# 选择列查询
tmp3 = session.query(Regionsale.sale).all()
for r3 in tmp3:
    print(r3.sale)
print("")
# 排序查询
tmp4 = session.query(Regionsale).filter(Regionsale.sale>10000).order_by(Regionsale.sale.asc()).all()
for r4 in tmp4:
    print(r4.province,r4.sale)
print("")
# 多表关联查询
tmp5 = session.query(Marttype,Regionsale).join(Regionsale,Marttype.id == Regionsale.id).all()
for r5 in tmp5:
    print(r5[0].type,r5[1].sale)
print("")
# 分组查询
tmp6 = session.query(
    Monthlysale.year,
    func.count(Monthlysale.month).label("Number"),
    func.max(Monthlysale.sale).label("MAX_sale"),
    func.min(Monthlysale.cost).label("MIN_cost")
    ).filter(Monthlysale.id>0).group_by(Monthlysale.year).all()
print("年份 个数 最大sale 最小cost")
for r6 in tmp6:
    print(r6.year,r6.Number,r6.MAX_sale,r6.MIN_cost)
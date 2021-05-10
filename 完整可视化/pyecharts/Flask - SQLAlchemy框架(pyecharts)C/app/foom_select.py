"""
    各种表查询
"""
from flask import Flask
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import *

app = Flask(__name__)

# 创建引擎
engine = create_engine("mysql+pymysql://root:123456@localhost:3306/web_01?charset=utf8")
# 创建基类
Base = declarative_base()
# 创建Session对象
Session = sessionmaker(bind=engine)
# 产生会话
session = Session()

class Table3_1(Base):
    __tablename__ = "table3_1"
    id = Column(Integer,primary_key=True)
    province = Column(String(12))
    city = Column(String(12))
    hotel_num = Column(Integer)
    room_num = Column(Integer)

class Table3_2(Base):
    __tablename__ = "table3_2"
    id = Column(Integer,primary_key=True)
    province = Column(String(12))
    norate = Column(Float)

# 通配符查询
tmp1 = session.query(Table3_1).filter(Table3_1.city.like("白%")).all()
for r1 in tmp1:
    print(r1.id,r1.city)
print("")
# 多条件查询
tmp2 = session.query(Table3_1).filter(and_(Table3_1.hotel_num>300,Table3_1.room_num<15000)).all()
for r2 in tmp2:
    print(r2.city,r2.hotel_num,r2.room_num)
print("")
# 多表关联查询
tmp3 = session.query(Table3_1,Table3_2).join(Table3_2,Table3_1.province == Table3_2.province).filter(Table3_2.norate>10.0).all()
for r3 in tmp3:
    print(r3[0].province,r3[0].room_num,r3[1].norate)
print("")
# 排序查询
tmp4 = session.query(Table3_1).filter(Table3_1.room_num>5000).order_by(Table3_1.hotel_num.desc())
for r4 in tmp4:
    print(r4.city,r4.hotel_num,r4.room_num)
print("")
# 选择列查询
tmp5 = session.query(Table3_2.province).all()
for r5 in tmp5:
    print(r5.province)
print("")
# 分组查询
tmp6 = session.query(
    Table3_1.province,
    func.sum(Table3_1.hotel_num).label("SUM_A"),
    func.avg(Table3_1.room_num).label("AVG_B")
    ).filter(Table3_1.hotel_num>10).group_by(Table3_1.province).all()
for r6 in tmp6:
    print(r6.province,r6.SUM_A,round(r6.AVG_B,1))
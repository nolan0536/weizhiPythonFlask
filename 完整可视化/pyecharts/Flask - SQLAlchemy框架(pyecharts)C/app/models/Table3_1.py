from app.settings import Base
from sqlalchemy import *

class Table3_1(Base):
    __tablename__ = "table3_1"
    id = Column(Integer,primary_key=True)
    province = Column(String(16))
    city = Column(String(16))
    hotel_num = Column(Integer)
    room_num = Column(Integer)
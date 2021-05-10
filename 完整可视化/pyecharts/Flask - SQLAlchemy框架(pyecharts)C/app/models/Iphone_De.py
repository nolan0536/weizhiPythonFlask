from app.settings import Base
from sqlalchemy import *

class Iphone_De(Base):
    __tablename__ = "iphone_de"
    id = Column(Integer,primary_key=True)
    编号 = Column(String(155))
    上限流量 = Column(Integer)
    下限流量 = Column(Integer)
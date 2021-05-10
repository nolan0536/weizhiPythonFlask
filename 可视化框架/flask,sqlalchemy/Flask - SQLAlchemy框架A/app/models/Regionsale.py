from app.settings import Base
from sqlalchemy import *

class Regionsale(Base):
    __tablename__ = "regionsale"
    id = Column(Integer,primary_key=True)
    province = Column(String(12))
    sale = Column(Integer)
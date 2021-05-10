from app.settings import Base
from sqlalchemy import *

class Table3_2(Base):
    __tablename__ = "table3_2"
    id = Column(Integer,primary_key=True)
    province = Column(String(15))
    norate = Column(Float)
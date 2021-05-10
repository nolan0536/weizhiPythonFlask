from app.settings import Base
from sqlalchemy import *

class Possword_B(Base):
    __tablename__ = "possword_b"
    id = Column(Integer,primary_key=True)
    password = Column(String(15))
    kid = Column(Integer)
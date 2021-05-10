from app.settings import Base
from sqlalchemy import *

class Radar_Data(Base):
    __tablename__ = "radar_data"
    id = Column(Integer,primary_key=True)
    section = Column(String(155))
    est_cost = Column(Integer)
    actu_expent = Column(Integer)

from sqlalchemy import Column, Integer

from database.db_setup import Base


class Lead(Base):
    __tablename__ = 'leads'
    lead_id = Column(Integer, primary_key=True)
    prob_convert = Column(Integer, )

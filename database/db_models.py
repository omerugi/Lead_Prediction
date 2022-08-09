from sqlalchemy import Column, Integer
from database.db_setup import Base

'''
The model for the table - leads.
Will contain the unique lead id + the predictions on that sample.
'''
class Lead(Base):
    __tablename__ = 'leads'
    lead_id = Column(Integer, primary_key=True, nullable=False)
    prob_convert = Column(Integer, nullable=False)

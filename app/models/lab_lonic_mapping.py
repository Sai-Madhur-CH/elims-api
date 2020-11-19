from sqlalchemy import Column
from sqlalchemy import String, Integer, DateTime
from db.connection import db
import datetime as dt


class LabLonicMapping(db.Model):

    __table_args__ = {'schema': 'config'}
    __table_name__ = 'lab_lonic_mapping'

    lab_id = Column(Integer, primary_key=True, autoincrement=True)
    loinc_num = Column(String, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=True, default=dt.datetime.now())
    updated_at = Column(DateTime, nullable=True, default=dt.datetime.now())
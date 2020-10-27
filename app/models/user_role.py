from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Boolean, Float, DateTime
from sqlalchemy.orm import relationship
from db.connection import db
import datetime as dt


class UserRoles(db.Model):

    __table_args__ = {'schema': 'config'}
    __table_name__ = 'user_roles'

    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=True, default=dt.datetime.now())
    updated_at = Column(DateTime, nullable=True, default=dt.datetime.now())

    def get_roles(self):
        roles = list(db.session.query(UserRoles).all())
        return [dict(row) for row in roles]

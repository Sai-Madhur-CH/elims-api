from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Boolean, Float, DateTime
from sqlalchemy.orm import relationship
from db.connection import db
import datetime as dt


class AppUsers(db.Model):

    __table_args__ = {'schema': 'config'}
    __table_name__ = 'app_users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey('config.user_role.role_id'), nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    hashed_password = Column(String, nullable=False)
    status = Column(String, nullable=False)
    last_login_date = Column(DateTime, nullable=True, default=dt.datetime.now())
    created_at = Column(DateTime, nullable=True, default=dt.datetime.now())
    updated_at = Column(DateTime, nullable=True, default=dt.datetime.now())


    def get_app_users(self):
        users = list(db.session.query(AppUsers).all())
        return [dict(row) for row in users]
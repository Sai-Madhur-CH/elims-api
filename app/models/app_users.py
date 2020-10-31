from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Boolean, Float, DateTime, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy import or_
from models.user_role import UserRoles
from db.connection import db
import datetime as dt

class AppUsers(db.Model):

    __table_args__ = {'schema': 'config'}
    __table_name__ = 'app_users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey(UserRoles.role_id), nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(BigInteger, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    status = Column(String, nullable=False)
    login_count = Column(Integer, nullable=True)
    login_attempts = Column(Integer, nullable=True)
    last_login_date = Column(DateTime, nullable=True, default=dt.datetime.now())
    created_at = Column(DateTime, nullable=True, default=dt.datetime.now())
    updated_at = Column(DateTime, nullable=True, default=dt.datetime.now())


    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def update_app_user(row):
        if row:
            user = db.session.query(AppUsers).filter_by(user_id = row.get('user_id')).first()
            for k, v in row.items():
                setattr(user, k, v)
        db.session.commit()

    def get_app_users(self):
        users = db.session.query(AppUsers.name,
                                 AppUsers.email,
                                 AppUsers.phone,
                                 AppUsers.role_id,
                                 AppUsers.created_at,
                                 AppUsers.updated_at,
                                 AppUsers.last_login_date,
                                 AppUsers.status,
                                 AppUsers.login_count,
                                 AppUsers.login_attempts,
                                 UserRoles.role_name
                                ).filter(
                                    UserRoles.role_id == AppUsers.role_id
                                ).all()
        return list(row._asdict() for row in users)
       

    def get_user(self, filters):
        user = db.session.query(AppUsers.user_id,
                                AppUsers.name,
                                AppUsers.email,
                                AppUsers.phone,
                                AppUsers.role_id,
                                AppUsers.created_at,
                                AppUsers.updated_at,
                                AppUsers.last_login_date,
                                AppUsers.status,
                                AppUsers.hashed_password,
                                AppUsers.login_count,
                                AppUsers.login_attempts,
                                UserRoles.role_name
                                ).filter_by(
                                    **filters
                                ).filter(
                                    UserRoles.role_id == AppUsers.role_id
                                ).first()
        if user:
            return user._asdict()
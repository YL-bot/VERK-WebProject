import sqlalchemy
from flask_login import UserMixin
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    projects = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    tasks = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    picture = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

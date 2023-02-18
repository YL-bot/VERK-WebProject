import sqlalchemy
from sqlalchemy import ForeignKey
from .db_session import SqlAlchemyBase


class Project(SqlAlchemyBase):
    __tablename__ = 'projects'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    users = sqlalchemy.Column(ForeignKey('users.id'), nullable=True)
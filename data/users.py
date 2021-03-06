import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.date.today())
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='Нет описания')
    avatar = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    amount_quiz = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    correct_answers_quiz = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    correct_answers_marathon = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    amount_marathon = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

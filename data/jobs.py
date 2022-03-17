import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Jobs(SqlAlchemyBase, UserMixin, SerializerMixin):
    # таблица, которая будет создана
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.Integer, default=datetime.datetime.now, nullable=True)
    end_date = sqlalchemy.Column(sqlalchemy.Integer, default=datetime.datetime.now, nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False, nullable=True)

    # получение полноценного объекта класса news для конкретного пользователя (можем обращаться к любому атрибуту)
    user = orm.relation("User", back_populates='job')

    # Важно! back_populates должно указывать не на таблицу, а на атрибут класса orm.relation!

    def __repr__(self):
        return f'{self.team_leader} {self.job} {self.work_size} {self.collaborators} {self.is_finished}' \


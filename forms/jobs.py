from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, BooleanField
# from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from flask_login import UserMixin


class AddJob(FlaskForm, UserMixin):
    team_leader = StringField('Тимлид', validators=[DataRequired()])
    job = StringField('Работа', validators=[DataRequired()])
    work_size = StringField('Размер работы', validators=[DataRequired()])
    collaborators = StringField('Коллабораторы', validators=[DataRequired()])
    is_finished = BooleanField('Работа выполнена?')
    submit = SubmitField('Войти')
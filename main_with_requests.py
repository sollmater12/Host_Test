import datetime

from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    # --------------------------------------
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.email = "scott_chief@mars.org"
    db_sess.add(user)
    db_sess.commit()
    # ------------------------------------

    # --------------------------------------
    user = User()
    user.surname = "Pitt"
    user.name = "Bread"
    user.age = 58
    user.position = 'navigator'
    user.speciality = 'research engineer'
    user.email = "bread_pitt@mars.org"
    db_sess.add(user)
    db_sess.commit()
    # ------------------------------------

    # --------------------------------------
    user = User()
    user.surname = "DiCaprio"
    user.name = "Leonardo"
    user.age = 47
    user.position = 'cook'
    user.speciality = 'research meal'
    user.email = "Di_Caprio@mars.org"
    db_sess.add(user)
    db_sess.commit()
    # ------------------------------------

    # --------------------------------------
    user = User()
    user.surname = "Cruise"
    user.name = "Tom"
    user.age = 60
    user.position = 'military'
    user.speciality = 'research war'
    user.email = "tom_cruise@mars.org"
    db_sess.add(user)
    db_sess.commit()
    # ------------------------------------

    # ------------------------------------
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    db_sess.add(job)
    db_sess.commit()
    # ------------------------------------

    # ------------------------------------
    job = Jobs()
    job.team_leader = 2
    job.job = 'deployment of residential modules 3 and 4'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = True
    db_sess.add(job)
    db_sess.commit()
    # ------------------------------------

    # ------------------------------------
    for user in db_sess.query(User):
        print("Запрос", user)

    for job in db_sess.query(Jobs):
        print('Работа', job)

    app.run()


if __name__ == '__main__':
    main()

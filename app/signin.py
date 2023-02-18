from app.data import db_session
from data.users import User
from flask import Flask

app = Flask(__name__)


def main():
    db_session.global_init('db/basa.db')
    user = User()
    user.login = "Пользователь 1"
    user.password = 'abc'
    user.email = "email1@email.ru"
    user.name = "Пользователь 1"
    user.projects = "a"
    user.tasks = "a"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()
from app.data import db_session
from data.users import User
from flask import Flask

app = Flask(__name__)


def main():
    db_session.global_init('db/basa.db')


if __name__ == '__main__':
    main()
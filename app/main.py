from app.data import db_session
from data.users import User
from flask import Flask, request, url_for, render_template

app = Flask(__name__)


def main():
    db_session.global_init('db/basa.db')


@app.route('/')
@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    main()
    app.run(port=8080, host='127.0.0.1')

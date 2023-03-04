from app.data import db_session
from data.users import User
from flask import Flask, redirect, render_template, request
from flask_login import LoginManager, logout_user, login_required

app = Flask(__name__)
# login_manager = LoginManager()
# login_manager.init_app(app)


def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    print(request.method)
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    db_session.global_init('db/basa.db')
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
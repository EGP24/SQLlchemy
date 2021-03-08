from data import db_session
from flask import Flask, render_template
from data.users import User
from data.jobs import Jobs
from form import LoginForm

db_session.global_init("db/base.db")
db_sess = db_session.create_session()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def empty():
    jobs = db_sess.query(Jobs).all()
    return render_template('empty.html', title='Список работ', jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        user = User()
        for key, value in form.__dict__.items():
            if key not in ['csrf_token', '_csrf', '_fields', '_prefix', 'meta']:
                setattr(user, key, value.data)
        db_sess.add(user)
        db_sess.commit()
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

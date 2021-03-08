from data import db_session
from flask import Flask, render_template
from data.users import User
from data.jobs import Jobs
from form import RegisterForm

db_session.global_init("db/base.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def empty():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template('empty.html', title='Список работ', jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.hashed_password.data == form.repeat_password.data:
            db_sess = db_session.create_session()
            keys = ['hashed_password', 'email', 'surname', 'name', 'age', 'position', 'speciality', 'address']
            user = User()
            for key in keys:
                setattr(user, key, getattr(form, key).data)
            db_sess.add(user)
            db_sess.commit()
            return render_template('register.html', title='Регистрация', form=form)
        return render_template('register.html', message='Different passwords', title='Регистрация', form=form)
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

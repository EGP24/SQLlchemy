from data import db_session
from flask import Flask, render_template
from data.jobs import Jobs

db_session.global_init("db/base.db")
db_sess = db_session.create_session()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def empty():
    jobs = db_sess.query(Jobs).all()
    return render_template('empty.html', title='Список работ', jobs=jobs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

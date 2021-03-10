from data import db_session
from data.users import User
import json

db_session.global_init("db/base.db")
db_sess = db_session.create_session()
with open('users.json', encoding='utf8') as file:
    data = json.load(file)

for user in data:
    db_user = User()
    for key, value in user.items():
        setattr(db_user, key, value)
    db_sess.add(db_user)
db_sess.commit()

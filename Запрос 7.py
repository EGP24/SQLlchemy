global_init(input())
db_sess = create_session()

for user in db_sess.query(User).filter(User.age < 21):
    user.address = 'module_3'
global_init(input())
db_sess = create_session()
for user in db_sess.query(User).filter(User.address == 'module_1'):
    print(user)
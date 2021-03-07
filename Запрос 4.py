global_init(input())
db_sess = create_session()
for user in db_sess.query(User).filter((User.position.like('%chief%') |
                                        User.position.like('%middle%'))):
    print(user, user.position)

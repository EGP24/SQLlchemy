global_init(input())
db_sess = create_session()
dct = {}
for job in db_sess.query(Jobs).all():
    dct.setdefault(len(job.collaborators.split(', ')), [])
    dct[len(job.collaborators.split(', '))].append(job.team_leader)

for user in db_sess.query(User).filter(User.id.in_(dct[max(dct)])):
    print(user.name, user.surname)
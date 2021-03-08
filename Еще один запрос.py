global_init(input())
db_sess = create_session()

ids = db_sess.query(Department).filter(Department.id == 1)[0]
ids = {key: 0 for key in list(map(int, ids.members.split(', ')))}
for job in db_sess.query(Jobs).all():
    new_ids = set(ids) & set(map(int, job.collaborators.split(', ')))
    if new_ids != set():
        for id in new_ids:
            ids[id] += job.work_size

for user in db_sess.query(User).filter(User.id.in_([i[0] for i in list(filter(lambda x: x[1] > 25, ids.items()))])):
    print(user.surname, user.name)

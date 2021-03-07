global_init(input())
db_sess = create_session()
for job in db_sess.query(Jobs).filter(Jobs.work_size < 20, Jobs.is_finished == 0):
    print('<Job>', job.job)

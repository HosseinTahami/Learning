from celery import Celery


app = Celery(
    main='app-celery',
    broker='amqp://guest:guest@localhost:5672'
)


'''First Way for Celery Config'''
# app.conf.task_always_eager = False

'''Second Way for Celery Config'''
# app.conf.update(
#     task_time_limit=20,
#     worker_concurrency=5,
#     worker_prefetch_multiplier=1,
# )

'''Third Way for Celery Config'''
app.config_from_object('celery_conf')


@app.task
def add(n1, n2):
    return n1 + n2

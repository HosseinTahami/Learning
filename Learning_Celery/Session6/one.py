from celery import Celery


app = Celery(
    main='app-celery',
    broker='amqp://guest:guest@localhost:5672'
)

app.config_from_object('celery_conf')


# app.conf.update(
#     task_time_limit=20,
#     worker_concurrency=5,
#     worker_prefetch_multiplier=1,
# )


@app.task
def add(n1, n2):
    return n1 + n2

from celery import Celery
import time


app = Celery(
    main='First',
    broker='amqp://guest:guest@localhost:5672'
)


@app.task(name='one.sum-of-two-number')
def add(n1, n2):
    time.sleep(15)
    return n1 + n2

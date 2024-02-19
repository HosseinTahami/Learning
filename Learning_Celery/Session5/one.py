from celery import Celery
import time

app = Celery(
    main='first-celery',
    broker='amqp://guest:guest@localhost:5672',
    backend='rpc://',  # RabbitMQ for getting results
)


@app.task
def multiply(n1, n2):
    time.sleep(7)
    return n1*n2


'''
PYTHON
---------

result = multiply.delay(3,5)

result.get()

result.status

'''

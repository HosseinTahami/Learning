from celery import Celery


app = Celery(
    main='one',
    broker='amqp://root:iran1379@localhost:5672',  # amqp://"username":"password"
)

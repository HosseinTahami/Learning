from celery import Celery
from celery.utils.log import get_task_logger

app = Celery(
    main='Number-one',
    broker='amqp://guest:guest@localhost:5672',
)
logger = get_task_logger(__name__)


@app.task(bind=True, default_retry_delay=600)
def divide(self, n1, n2):
    print(self.request)
    try:
        return n1 / n2
    except ZeroDivisionError:
        print('Second Number is ...')
        logger.info('Sorry..!')
        self.retry(count_down=10, max_retries=10)

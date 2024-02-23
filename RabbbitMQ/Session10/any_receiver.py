import pika
from pika.exchange_type import ExchangeType as et

credentials = pika.PlainCredentials(
    username='root',
    password='iran1379',
)

parameters = pika.ConnectionParameters(
    host='localhost',
    credentials=credentials,
)

connection = pika.BlockingConnection(
    parameters=parameters
)


channel = connection.channel()

channel.exchange_declare(
    exchange='headers_logs',
    exchange_type=et.headers,
)

channel.queue_declare(
    queue='any-queue',
)

bind_arguments = {
    'x-match': 'any',
    'first-name': 'Hossein',
    'age': 78,
}

channel.queue_bind(
    queue='any-queue',
    exchange='headers_logs',
    arguments=bind_arguments
)


def callback(ch, method, properties, body):
    print(f'Received {body}')


channel.basic_consume(
    queue='any-queue',
    auto_ack=True,
    on_message_callback=callback
)

print('Waiting for messages...')
channel.start_consuming()


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
    parameters=parameters,
)


channel = connection.channel()

channel.exchange_declare(
    exchange='headers_logs',
    exchange_type=et.headers
)

message = 'Header Type Message..!'

properties = pika.BasicProperties(
    headers={
        'first-name': 'Hossein',
        'age': 23,
    }
)

print('Message Sent..!')

channel.basic_publish(
    exchange='headers_logs',
    body=message,
    routing_key='',
    properties=properties
)

connection.close()

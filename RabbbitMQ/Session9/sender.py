import pika

credentials = pika.PlainCredentials(
    username='root',
    password='iran1379'
)

parameters = pika.ConnectionParameters(
    host='localhost',
    credentials=credentials
)

connection = pika.BlockingConnection(
    parameters=parameters
)

channel = connection.channel()

channel.exchange_declare(
    exchange_type='topic',
    exchange='topic_logs'
)

messages = {
    'error.warning.important': 'important message',
    'info.debug.unimportant': 'unimportant message',
}

for key, value in messages.items():
    channel.basic_publish(
        exchange='topic_logs',
        routing_key=key,
        body=value
    )

print('Message Sent..!')
connection.close()

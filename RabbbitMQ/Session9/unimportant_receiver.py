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
    exchange='topic_logs',
)

result = channel.queue_declare(
    queue='',
    exclusive=True,
)

channel.queue_bind(
    queue=result.method.queue,
    exchange='topic_logs',
    routing_key='*.*.unimportant',
)


print(f''' 
Waiting for unimportant messages in {result.method.queue}
'''
      )


def callback(ch, method, properties, body):
    print(body)


channel.basic_consume(
    queue=result.method.queue,
    on_message_callback=callback,
    auto_ack=True,
)

channel.start_consuming()

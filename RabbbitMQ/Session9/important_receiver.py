import pika

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
    exchange='topic_logs',
    exchange_type='topic',
)

result = channel.queue_declare(
    queue='',  # empty string means random name queue
    exclusive=True,
)

channel.queue_bind(
    exchange='topic_logs',
    queue=result.method.queue,
    routing_key='*.*.important',
)

print(f''' 
Waiting for important messages in {result.method.queue}
'''
      )


def callback(ch, method, properties, body):
    with open('error_logs.log', 'a') as error_log:
        error_log.write(f'{str(body)} \n')


channel.basic_consume(
    queue=result.method.queue,
    on_message_callback=callback,
    auto_ack=True,

)

channel.start_consuming()

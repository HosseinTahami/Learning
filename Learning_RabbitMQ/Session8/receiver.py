import pika

credentials = pika.PlainCredentials(
    username="root",
    password="iran1379"
)

parameters = pika.ConnectionParameters(
    credentials=credentials,
    host='localhost'
)

connection = pika.BlockingConnection(
    parameters=parameters
)

channel = connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)

''' exclusive decide if the queue that was created will be deleted each time
    after the message was sent or not
'''
result = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='logs', queue=result.method.queue)

print('Waiting for logs...')
print(result.method.queue)


def callback(ch, method, properties, body):
    print(f'Received {body}')


channel.basic_consume(queue=result.method.queue,
                      on_message_callback=callback, auto_ack=True)

channel.start_consuming()

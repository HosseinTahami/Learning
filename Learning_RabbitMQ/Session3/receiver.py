import pika

''' Create a connection'''

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost'
        )
    )

''' Create a Channel'''

channel = connection.channel()

''' Create or Declare a queue for the channel that we want to work with it !'''

channel.queue_declare(
    queue='one'
)

''' A CallBack Function so when the message is received it will go there !'''

def callback(ch, method, properties, body):
    print(f'Received {body}')

channel.basic_consume(queue='one', on_message_callback=callback, auto_ack=True)

print('Waiting for message Enter ctrl+c to Exit !')

channel.start_consuming()
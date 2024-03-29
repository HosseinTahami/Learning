import pika


''' Create a connection'''
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost'
    )
)

''' Create a Channel'''
channel = connection.channel()


''' Create or Declare a queue for the channel
    that we want to work with !
'''
channel.queue_declare(
    queue='one'
)


''' A CallBack Function so when the message is received
    this function will be executed !
    The callback method should have ch as channel
    method, properties and body for argument !
'''


def callback(ch, method, properties, body):
    print(f'Received {body}')


''' basic_consume will read the messages
    from the Broker and execute them
    queue argument is the name of the channel
    on_message_callback is for choosing the method that
    we want to be executed after receiving the message.
    auto_ack or auto acknowledge will tell the broker that
    I have received the message so delete it from queue.
'''
channel.basic_consume(queue='one', on_message_callback=callback, auto_ack=True)


print('''Waiting for message
         Enter ctrl+c to Exit !''')


'''This will start the Receiving Process'''
channel.start_consuming()

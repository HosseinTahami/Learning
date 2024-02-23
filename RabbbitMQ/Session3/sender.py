import pika


''' First we are creating a connection'''
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
    )
)

''' Create a channel for the connection '''

channel = connection.channel()


''' Create a queue or declare which queue is the one we want !
    queue_declare will create a queue if needed
    or connect to a queue if there is one
'''
channel.queue_declare(queue='one')


''' basic_publish will publish sth inside the channel we have.
    exchange argument is for the type of our exchange method
    routing_key argument is for the queue name
    body argument is the thing we want to publish
'''
channel.basic_publish(
    exchange='',
    routing_key='one',
    body='hello world !'
)

'''We always have to close our connection'''
connection.close()

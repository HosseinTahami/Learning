import pika

credentials = pika.PlainCredentials('root', 'iran1379')

''' First we are creating a connection'''
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        credentials=credentials
        )
    )

''' create a channel for the connection '''
channel = connection.channel()


''' create a queue or declare which queue is the one we want !'''
''' queue_declare will create a queue if needed o
    or connect to a queue if there is one
'''
channel.queue_declare(queue='one')

channel.basic_publish(
    exchange='',
    routing_key='one',
    body='hello world !'
    )

connection.close()
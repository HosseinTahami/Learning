import pika
import time

''' If you want to use rabbitmq through a specific user
    you have to give the user credential with PlainCredential
    Then use these credentials in your connection
'''
credentials = pika.PlainCredentials('root', 'iran1379')


''' First we are creating a connection'''
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        credentials=credentials,
    )
)

''' Create a channel for the connection '''

channel = connection.channel()


''' Create a queue or declare which queue is the one we want !
    queue_declare will create a queue if needed
    or connect to a queue if there is one
'''
channel.queue_declare(queue='one')


''' properties are more information about the data we are sending
    content_type is for the type of our data
    content_encoding is for the type of compressing methods
    timestamp is for the time we create the message we are sending
    expiration is for the time our message will be expired
    and the broker will delete it.
    delivery_mode is 1 or 2 and means do you want to save messages
    on disk or only RAM, 1 is for RAM and 2 is for saving on disk.
    user_id & app_id  is more information about the publisher and ...
    type is application-specific message type (exchange_name.queue_name)
    headers are more info you want to send next to your message
'''

properties = pika.BasicProperties(
    # content_type='text/plain',
    # content_encoding='gzip',
    # timestamp=40000000000,
    # expiration=str(time.time()),
    # delivery_mode=2,
    # user_id="10",
    # app_id="3",
    # type="exch.queue",
    headers={"name": "Hossein", "age": 34}
)


''' basic_publish will publish sth inside the channel we have.
    exchange argument is for the type of our exchange method
    routing_key argument is for the queue name
    body argument is the thing we want to publish
'''
channel.basic_publish(
    exchange='',
    routing_key='one',
    body='hello world !',
    properties=properties
)

print("Message sent !")

'''We always have to close our connection'''
connection.close()

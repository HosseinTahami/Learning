import pika


credentials = pika.PlainCredentials(
    username='root',
    password='iran1379'
)

parameters = pika.ConnectionParameters(
    host='localhost',
    credentials=credentials
)

connection = pika.BlockingConnection(parameters=parameters)

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')
channel.basic_publish(exchange='logs', routing_key='',
                      body='This is FANOUT..!')
print("message Sent")
channel.close()

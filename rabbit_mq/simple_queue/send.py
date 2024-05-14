import pika

# Connects to the broker on the local machine
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declares a queue -> queue is a pipeline where all the messages will be sent (FIFO)
channel.queue_declare(queue='hello')

# Message can never directly be sent to a queue
# Some sort of exchange needs to happen
# Routing key is the name of the queue the message needs to be sent to.
channel.basic_publish(
        exchange='',
        routing_key='hello',
        body='Hello World!'
    )
print(" [x] sent 'Hello World'")

# Close the connection so the message is delivered.
connection.close()


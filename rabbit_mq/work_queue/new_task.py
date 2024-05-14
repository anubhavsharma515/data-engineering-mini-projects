import sys, pika

# Either check for the first CLI arg passed or assing "Hello World!"
message = ' '.join(sys.argv[1:]) or "Hello World!"

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(
        exchange='',
        routing_key='hello',
        body=message
)

print(f" [x] sent '{message}'")

connection.close()

import pika, time, sys, os


# This file defines the consumer, which waits for a message and essentially does the work.
# By default, Rabbit distributes messages over multiple consumers (workers in this context)
# through round-robin.
def main():
    # Connect to the broker
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declares a queue -> queue is a pipeline where all the messages will be sent (FIFO)
    # This command is idempotent -> we can keep running it, only one will be created
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):

        print(f" [x] Received {body}")
        # Fake a second of work - pretend to be busy by sleeping for every '.' in the message
        time.sleep(body.count(b'.'))
        print(f" [x] Done.")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    # We enter a never-ending loop that waits for data and runs callbacks whenever necessary
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

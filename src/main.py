from settings import settings
import pika

if __name__ == '__main__':
    print(settings.RMQ_SETTINGS['dsn'])
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')
    for _ in range(10):
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=b'Hello World!')
        print(" [x] Sent 'Hello World!'")
    connection.close()

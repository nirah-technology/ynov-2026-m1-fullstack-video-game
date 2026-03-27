import pika
from threading import Thread

class MessageConsumer:
    @staticmethod
    def subscribe(queue_name: str, callback: callable):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, virtual_host='/', credentials=pika.PlainCredentials('guest', 'guest')))
        channel = connection.channel()
        channel.queue_declare(queue=queue_name, durable=True, arguments={'x-queue-type': 'quorum'})
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        thread = Thread(target=channel.start_consuming)
        thread.start()


class MessagePublisher:
    @staticmethod
    def send_message(message: str, queue_name: str):
        connection =  pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=queue_name, durable=True, arguments={'x-queue-type': 'quorum'})
        channel.basic_publish(exchange='', routing_key=queue_name, body=message)

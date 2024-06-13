import pika
import sys
from dotenv import load_dotenv
import os

load_dotenv()


class Subscriber:
    def __init__(self, queueName, bindingKey, config):
        self.queueName = queueName
        self.bindingKey = bindingKey
        self.config = config
        self.connection = self._create_connection()

    def __del__(self):
        self.connection.close()

    def _create_connection(self):
        credentials = pika.PlainCredentials(
            self.config["user"], self.config["password"]
        )
        parameters = pika.ConnectionParameters(
            self.config["host"], self.config["port"], "/", credentials
        )
        return pika.BlockingConnection(parameters)

    def on_message_callback(self, channel, method, properties, body):
        binding_key = method.routing_key
        print("received new message for - " + binding_key)
        print(f" [x] Received {body}")

    def setup(self):
        channel = self.connection.channel()
        channel.exchange_declare(
            exchange=self.config["exchange"], exchange_type="topic"
        )
        # This method creates or checks a queue
        channel.queue_declare(queue=self.queueName)
        # Binds the queue to the specified exchang
        channel.queue_bind(
            queue=self.queueName,
            exchange=self.config["exchange"],
            routing_key=self.bindingKey,
        )
        channel.basic_consume(
            queue=self.queueName,
            on_message_callback=self.on_message_callback,
            auto_ack=True,
        )
        print(" [*] Waiting for data for " + self.queueName + ". To exit press CTRL+C")
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()


config = {
    "host": os.getenv("RMQ-HOST"),
    "port": os.getenv("RMQ-PORT"),
    "exchange": os.getenv("RMQ-EXCHANGE"),
    "user": os.getenv("RMQ-USER"),
    "password": os.getenv("RMQ-PASS"),
}

queueName = os.getenv("RMQ-EXCHANGE")
# key in the form exchange.*
key = '*'
subscriber = Subscriber(queueName, key, config)
subscriber.setup()

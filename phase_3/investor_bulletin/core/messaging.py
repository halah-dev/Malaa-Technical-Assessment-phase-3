import pika
import os
from dotenv import load_dotenv
import json
from faker import Faker
import random
import requests

load_dotenv()
fake = Faker()


class Publisher:
    def __init__(self, config):
        self.config = {
            "host": os.getenv("RMQ-HOST"),
            "port": os.getenv("RMQ-PORT"),
            "exchange": os.getenv("RMQ-EXCHANGE"),
            "user": os.getenv("RMQ-USER"),
            "password": os.getenv("RMQ-PASS"),
        }

    def publish(self, routing_key, message):
        connection = self.create_connection()
        # Create a new channel with the next available channel number or pass in a channel number to use channel =
        channel = connection.channel()
        channel.queue_declare(queue=self.config["exchange"])
        # Creates an exchange if it does not already exist, and if the exchange exists,
        # verifies that it is of the correct and expected class.
        channel.exchange_declare(
            exchange=self.config["exchange"], exchange_type="topic"
        )

        # Publishes message to the exchange with the given routing key
        channel.basic_publish(
            exchange=self.config["exchange"],
            routing_key=routing_key,
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ),
        )
        print(" [x] Sent message %r for %r" % (message, routing_key))

    # Create new connection
    def create_connection(self):
        credentials = pika.PlainCredentials(
            self.config["user"], self.config["password"]
        )
        parameters = pika.ConnectionParameters(
            self.config["host"], self.config["port"], "/", credentials
        )
        return pika.BlockingConnection(parameters)


symbols = ["AAPL", "MSFT", "GOOG", "AMZN", "META"]
response = requests.request(
    "POST",
    "http://localhost:8000/alert-rules",
    json={
        "name": fake.name(),
        "threshold_price": round(random.uniform(1.0, 500.0), 2),
        "symbol": random.choice(symbols),
    },
)
message = response.json()

publisher = Publisher()
publisher.publish(os.getenv("RMQ-ROUTING-KEY"), message)

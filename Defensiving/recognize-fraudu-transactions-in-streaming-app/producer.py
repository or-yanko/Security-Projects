import os
import json
from time import sleep
from kafka import KafkaProducer
from settings import *
from transactions import create_random_transaction

if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL,
                             value_serializer=lambda value: json.dumps(value).encode(),)
    while True:
        transaction: dict = create_random_transaction()
        producer.send(TRANSACTIONS_TOPIC, value=transaction)
        print(transaction)
        sleep(SLEEP_TIME)

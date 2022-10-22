KAFKA_BROKER_URL = "localhost:9092"
TRANSACTIONS_TOPIC = "queuing.transactions"
TRANSACTIONS_PER_SECOND = float("2.0")
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND
LEGIT_TOPIC = "queuing.legit"
FRAUD_TOPIC = "queuing.fraud"

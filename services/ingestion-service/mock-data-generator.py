from faker import Faker
import json
import time
import random
from kafka import KafkaProducer

fake = Faker()
producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda x: json.dumps(x).encode('utf-8'))

def generate_mock_data():
    while True:
        data = {
            "user_id": fake.uuid4(),
            "name": fake.name(),
            "email": fake.email(),
            "event_type": random.choice(["click", "view", "purchase"]),
            "timestamp": fake.iso8601(),
            "metadata": fake.pydict(5)
        }
        producer.send("events",value=data)
        time.sleep(1)

if __name__ == "__main__":
    generate_mock_data()

from kafka import KafkaProducer
import json

topic = "foobar"
# Serialize json messages
producer = KafkaProducer(bootstrap_servers='localhost:29092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for x in range(10):
    print("x", x)
    # Use a dict as value
    producer.send(topic, {'key1': 'value1', 'key2': x})

# Block until all pending messages are at least put on the network
# NOTE: This does not guarantee delivery or success! It is really
# only useful if you configure internal batching using linger_ms
producer.flush()


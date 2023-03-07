from kafka import KafkaConsumer, TopicPartition
import msgpack

topic = 'foobar'

# Deserialize msgpack-encoded values
consumer = KafkaConsumer(bootstrap_servers='localhost:29092', value_deserializer=msgpack.loads)
consumer.subscribe([topic])

for msg in consumer:
    print(msg)
    assert isinstance(msg.value, dict)



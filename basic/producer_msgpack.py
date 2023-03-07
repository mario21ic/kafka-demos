from kafka import KafkaProducer
import msgpack

topic = "foobar"

# encode objects via msgpack
producer = KafkaProducer(bootstrap_servers='localhost:29092', value_serializer=msgpack.dumps)
producer.send(topic, {'mykey': 'myvalue', 'x': 123})

# Block until all pending messages are at least put on the network
# NOTE: This does not guarantee delivery or success! It is really
# only useful if you configure internal batching using linger_ms
producer.flush()


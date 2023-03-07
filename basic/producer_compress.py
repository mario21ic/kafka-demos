from kafka import KafkaProducer

topic = "foobar"
producer = KafkaProducer(bootstrap_servers='localhost:29092', compression_type='gzip')

for x in range(10):
    print("x", x)
    producer.send(topic, b'msg %d' % x)

# Block until all pending messages are at least put on the network
# NOTE: This does not guarantee delivery or success! It is really
# only useful if you configure internal batching using linger_ms
producer.flush()


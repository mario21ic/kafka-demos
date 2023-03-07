from kafka import KafkaProducer

topic = "foobar"

producer = KafkaProducer(bootstrap_servers='localhost:29092', key_serializer=str.encode)
for x in range(10):
    print("x", x)
    # Use a key for hashe-partitioning
    producer.send(topic, key=b'mykey', value=b'message_x_' + str(x).encode())

# Block until all pending messages are at least put on the network
# NOTE: This does not guarantee delivery or success! It is really
# only useful if you configure internal batching using linger_ms
producer.flush()


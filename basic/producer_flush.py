from kafka import KafkaProducer

topic = "foobar"

producer = KafkaProducer(bootstrap_servers='localhost:29092')
for x in range(100):
    print("x", x)
    producer.send(topic, b"some_message_bytes_x_" + str(x).encode())

# Block until all pending messages are at least put on the network
# NOTE: This does not guarantee delivery or success! It is really
# only useful if you configure internal batching using linger_ms
producer.flush()



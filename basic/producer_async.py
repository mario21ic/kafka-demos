from kafka import KafkaProducer

topic = "foobar"

producer = KafkaProducer(bootstrap_servers='localhost:29092')
for x in range(100):
    print("x", x)
    # Async
    producer.send(topic, b"some_message_bytes_x_" + str(x).encode())


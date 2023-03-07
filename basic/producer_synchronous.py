from kafka import KafkaProducer

topic = "foobar"

producer = KafkaProducer(bootstrap_servers='localhost:29092')
for x in range(10):
    print("x", x)
    # Block until a single message is sent (or timeout)
    future = producer.send('foobar', b'some_message_bytes_x_' + str(x).encode())
    #record_metada = future.get(timeout=10)
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        #log.exception()
        pass
    # Successful result returns assigned partition and offset
    print("topic:", record_metadata.topic)
    print("partition:", record_metadata.partition)
    print("offset:", record_metadata.offset)



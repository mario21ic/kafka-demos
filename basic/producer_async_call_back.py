from kafka import KafkaProducer

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception



topic = "foobar"
#topic = "test-topic2"

# configure multiple retries
producer = KafkaProducer(
    bootstrap_servers=['localhost:29092', 'localhost:39092', 'localhost:49092'],
    retries=5)

for x in range(10):
    print("x", x)
    # produce asynchronously with callbacks
    producer.send(topic, b'raw_bytes_x_' + str(x).encode()).add_callback(on_send_success).add_errback(on_send_error)

# block until all async messages are sent
producer.flush()



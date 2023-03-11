#!/usr/bin/env python
# syntax: topic qty
# example: ./producer_async_call_back.py weblog 100

from kafka import KafkaProducer
import sys

def on_send_success(record_metadata):
    print('='*5)
    print('topic:', record_metadata.topic)
    print('partition:', record_metadata.partition)
    print('offset:', record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception


topic = "foobar"
if sys.argv[1] is not None:
    topic = sys.argv[1]
print("topic:", topic)

qty = 10
if sys.argv[2] is not None:
    qty = int(sys.argv[2])
print("qty:", qty)

# configure multiple retries
producer = KafkaProducer(
        bootstrap_servers=['localhost:29092', 'localhost:39092', 'localhost:49092'],
        retries=5)

for x in range(qty):
    print("x", x)
    # produce asynchronously with callbacks
    producer.send(topic, b'raw_bytes_x_' + str(x).encode()).add_callback(on_send_success).add_errback(on_send_error)

# block until all async messages are sent
producer.flush()



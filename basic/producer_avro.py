#!/usr/bin/env python
# syntax: topic qty
# example: ./producer_avro.py weblog 100

import sys
from kafka import KafkaProducer


import io
import random
import avro.schema
from avro.io import DatumWriter

topic = "foobar"
if sys.argv[1] is not None:
    topic = sys.argv[1]
print("topic:", topic)

qty = 10
if sys.argv[2] is not None:
    qty = int(sys.argv[2])
print("qty:", qty)

# Path to user.avsc avro schema
schema_path = "user.avsc"
schema = avro.schema.parse(open(schema_path).read())

producer = KafkaProducer(bootstrap_servers='localhost:29092')

for x in range(qty):
    print("x", x)
    writer = DatumWriter(schema)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write({"name": "12%s" % x, "favorite_color": "111", "favorite_number": random.randint(0, 10)}, encoder)
    raw_bytes = bytes_writer.getvalue()
    producer.send(topic, raw_bytes)

# Block until all pending messages are at least put on the network
# NOTE: This does not guarantee delivery or success! It is really
# only useful if you configure internal batching using linger_ms
producer.flush()


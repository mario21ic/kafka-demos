#!/usr/bin/env python

import sys
from kafka import KafkaConsumer

import io
import avro.schema
from avro.io import DatumReader, BinaryDecoder
from avro.datafile import DataFileReader

topic = 'foobar'
if sys.argv[1] is not None:
    topic = sys.argv[1]
print("topic:", topic)


consumer = KafkaConsumer(topic, 
        group_id='my_group',
        bootstrap_servers=['localhost:29092', 'localhost:39092', 'localhost:49092'],
        )
schema_path = "user.avsc"
schema = avro.schema.parse(open(schema_path).read())

for message in consumer:
    #print(msg)
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    bytes_reader = io.BytesIO(message.value)
    decoder = BinaryDecoder(bytes_reader)
    reader = DatumReader(schema)
    value = reader.read(decoder)
    #print('user:', user1)
    print("topic=%s partition=%d offset=%d key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          value))


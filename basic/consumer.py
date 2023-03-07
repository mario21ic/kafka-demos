from kafka import KafkaConsumer

topic = 'foobar'
consumer = KafkaConsumer(topic, 
    bootstrap_servers=['localhost:29092', 'localhost:39092', 'localhost:49092'],
    )
# consume earliest available messages, don't commit offsets
#KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)
# StopIteration if no message after 1sec
#KafkaConsumer(consumer_timeout_ms=1000)
# Subscribe to a regex topic pattern
#consumer.subscribe(pattern='^awesome.*')

"""
# Use multiple consumers in parallel w/ 0.9 kafka brokers
# typically you would run each on a different server / process / CPU
consumer1 = KafkaConsumer('my-topic',
                          group_id='my-group',
                          bootstrap_servers='my.server.com')
consumer2 = KafkaConsumer('my-topic',
                          group_id='my-group',
                          bootstrap_servers='my.server.com')
"""

for message in consumer:
    #print(msg)
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))



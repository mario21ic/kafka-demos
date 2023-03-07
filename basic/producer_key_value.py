from kafka import KafkaProducer
import random

#topic = "foobar"
# kafka-topics --bootstrap-server localhost:9092 --create --topic test-topic33 --replication-factor 3 --partitions 3
# kafka-console-producer  --bootstrap-server localhost:9092 --topic test-topic33 --property "key.separator=," --property "parse.key=true"
# 0,1
# 1,1
# 2,1
# 3,1
topic = "test-topic33"
brokers = 3

producer = KafkaProducer(bootstrap_servers='localhost:29092')
x = 0
for y in range(10):
    print("x: %s y: %s" % (x, y))
    x = random.randint(0, brokers)
    # Use a key for hashe-partitioning
    #producer.send(topic, headers=[(b'z', b'1')], key=b'mykey' + str(x).encode(), value=b'message_x_%d_y_%d' % (x, y))
    producer.send(topic, key=b'mykey' + str(x).encode(), value=b'message_x_%d_y_%d' % (x, y))

# Block until all pending messages are at least put on the network
# NOTE: This does not guarantee delivery or success! It is really
# only useful if you configure internal batching using linger_ms
producer.flush()


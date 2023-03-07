from kafka import KafkaConsumer, TopicPartition

topic = 'foobar'

consumer = KafkaConsumer(bootstrap_servers='localhost:29092')
# manually assign the partition list for the consumer
consumer.assign([TopicPartition(topic, 2)])

for msg in consumer:
    print(msg)


from kafka import KafkaConsumer

topic = 'foobar'
consumer = KafkaConsumer(topic, bootstrap_servers='localhost:29092')

for msg in consumer:
    print(msg)


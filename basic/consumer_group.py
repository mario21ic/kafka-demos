from kafka import KafkaConsumer

topic = 'foobar'

# join a consumer group for dynamic partition assignment and offset commits
consumer = KafkaConsumer(topic, group_id='my_favorite_group', bootstrap_servers='localhost:29092')

for msg in consumer:
    print(msg)


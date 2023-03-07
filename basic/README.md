```
docker compose up -d

docker compose exec kafka01 bash
#docker exec -ti kafka01 bash

kafka-topics --bootstrap-server localhost:9092 --list

kafka-topics --bootstrap-server localhost:9092 \
    --create \
    --topic weblog

kafka-topics --bootstrap-server localhost:9092 \
    --create \
    --topic test-topic \
    --replication-factor 1 \
    --partitions 4

kafka-topics --bootstrap-server localhost:9092 \
    --describe \
    --topic test-topic

kafka-topics --bootstrap-server localhost:9092 --create --topic test-topic2 --replication-factor 2 --partitions 4
kafka-topics --bootstrap-server localhost:9092 --delete --topic test-topic2
```

Replication depende del nro de nodos kafka
```
kafka-topics --bootstrap-server localhost:9092 --create --topic test-topic4 --replication-factor 4 --partitions 4
kafka-topics --bootstrap-server localhost:9092 --create --topic test-topic3 --replication-factor 3 --partitions 4
```

Producer:
```
kafka-console-producer --bootstrap-server localhost:9092 --topic weblog

kafka-console-producer  --bootstrap-server localhost:9092 --topic weblog --property "key.separator=:" --property "parse.key=true"
```

Consumer:
```
kafka-console-consumer \
    --bootstrap-server kafka01:9092 \
    --topic weblog  \
    --from-beginning \
    --property print.headers=true \
    --property print.timestamp=true

kafka-console-consumer \
    --bootstrap-server kafka01:9092 \
    --topic weblog  \
    --group "consumer01" \
    --from-beginning
```

Consumer groups:
```
kafka-consumer-groups --bootstrap-server localhost:9092 --list

kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group gapplication
kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group gapplication-01
```


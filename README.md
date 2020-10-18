![Python application](https://github.com/JacekPs/pyafka/workflows/Python%20application/badge.svg)
![Upload Python Package](https://github.com/JacekPs/pyafka/workflows/Upload%20Python%20Package/badge.svg)

# pyafka
Pyafka is a utility to receive Kafka events in python service. It uses confluent_kafka under the hood.
Grab it from Pypi:
https://pypi.org/project/pyafka/


To use - annotate your handler method as follows:

```
@kafka_consumer("broker_url", ["my_topic", "some_other_topic])
def handler(message):
    print(message.value())
```
You can pass additional arguments to '@kafka_consumer decorator'.

1: Specify kafka consumer group (defaut group is random UUID):
```
@kafka_consumer("broker_url", ["my_topic", "my_other_topic], group_id="my_group_id")
def handler(message):
    print(message.value())
```

2: Specify payload deserializer. Currently available are BytesDeserializer and StringDeserializer (default)  
```
@kafka_consumer("broker_url", ["my_topic", "my_other_topic], deserializer=BytesDeserializer().deserialize")
def handler(message):
    print(message.value())
```

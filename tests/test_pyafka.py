from pyafkalib.pyafka import kafka_consumer
from time import time, sleep

SOME_MESSAGE = 'some message'

def test_kafka_consumer(mocker):
    class Message:
        def value(self):
            return SOME_MESSAGE
    mocker.patch('confluent_kafka.DeserializingConsumer.__init__', return_value = None)
    mocker.patch('confluent_kafka.DeserializingConsumer.subscribe')
    mocker.patch('confluent_kafka.DeserializingConsumer.poll', side_effect = [Message(), Exception()])
    mocker.patch('confluent_kafka.DeserializingConsumer.commit', return_value = None)

    received_value = None

    @kafka_consumer('some_broker', ['some_topic'], 'some_group_id')
    def handler(message):
        nonlocal received_value
        received_value = message.value()

    start = time()
    while received_value is None and time() - start < 1:
        sleep(0.1)
    assert received_value == SOME_MESSAGE

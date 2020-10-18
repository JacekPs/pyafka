
import uuid
import threading
import logging

from confluent_kafka import DeserializingConsumer
from pyafkalib.deserializers import StringDeserializer


def kafka_consumer(bootstrap_servers : str, topics: list, group_id: str = None, deserializer = None, daemonic: bool = None) -> callable:
    if group_id is None:
        group_id = str(uuid.uuid4())
    if deserializer is None:
        deserializer = StringDeserializer().deserialize
    def kafka_consumer_decorator(handler):
        consumer = DeserializingConsumer(
            {"bootstrap.servers": bootstrap_servers,
             "group.id": group_id,
             "value.deserializer": deserializer})
        consumer.subscribe(topics)
        def consume():
            logging.debug(f'Initialized kafka_consumer for topics: \'{topics}\'')
            while (True):
                try:
                    event = consumer.poll()
                    logging.debug(f'Consuming event: \'{event.value()}\'')
                    handler(event)
                except Exception as e:
                    logging.exception(e)
                finally:
                    consumer.commit()
        thread = threading.Thread(target=consume)
        thread.setDaemon(daemonic)
        thread.start()
    return kafka_consumer_decorator

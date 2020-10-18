from confluent_kafka.serialization import SerializationContext

class BytesDeserializer:
    def deserialize(self, data: bytes, ctx: SerializationContext) -> bytes:
        return data

class StringDeserializer:
    def __init__(self, encoding: str = 'utf-8'):
        self.encoding = encoding

    def deserialize(self, data: bytes, ctx: SerializationContext) -> str:
        return data.decode(self.encoding)

from aiokafka import AIOKafkaProducer
from fastavro import writer
from io import BytesIO

from config.settings import logger
from .schema_registry import SchemaRegistryClient


async def send_one_message(
    topic: str,
    message: dict,
    key: str,
):

    client = SchemaRegistryClient()

    parsed_schema = client.validate_command(message)

    if not parsed_schema:
        logger.error(f"Сообщение не соответствует схеме: {message}")
        return False

    avro_bytes_io = BytesIO()
    writer(avro_bytes_io, parsed_schema, [message])
    avro_bytes = avro_bytes_io.getvalue()

    producer = AIOKafkaProducer(bootstrap_servers="broker:9092")

    await producer.start()
    try:
        await producer.send(
            topic,
            key=key.encode(),
            value=avro_bytes
        )
    except Exception as e:
        logger.error(f"Ошибка отправки сообщения: {e}")
    finally:
        await producer.stop()

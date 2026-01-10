from aiokafka import AIOKafkaProducer

from config.settings import logger


async def send_one_message(
    topic: str,
    message: str,
    key: str,
):
    producer = AIOKafkaProducer(bootstrap_servers="broker:9092")

    await producer.start()
    try:
        await producer.send(
            topic,
            key=key.encode(),
            value=message.encode()
        )
    except Exception as e:
        logger.error(f"Ошибка отправки сообщения: {e}")
    finally:
        await producer.stop()

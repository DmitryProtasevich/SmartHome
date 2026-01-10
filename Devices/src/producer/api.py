from config.kafka import send_one_message
from ninja import Router

from producer.schemas import KafkaMessage, KafkaResponse
from config.settings import logger


producer_router = Router()


@producer_router.post(
    path="/send-messages",
    tags=["produce"],
    response={200: KafkaResponse, 400: KafkaResponse, 500: KafkaResponse}
)
async def send_message(
    request,
    request_data: KafkaMessage,
) -> KafkaResponse:
    """Отправляет сообщения в кафку."""
    try:
        topic = request_data.topic
        key = request_data.key

        await send_one_message(
            topic,
            request_data.message,
            key
        )
        return KafkaResponse(
            status="success",
            message=f"Сообщение отправлено в топик {topic}",
            topic=topic,
            key=key
        )
    except Exception as e:
        logger.error(f"Ошибка при отправке: {e}")
        return KafkaResponse(
            status="error",
            message="Не удалось отправить сообщение в Kafka",
            error=str(e)
        )

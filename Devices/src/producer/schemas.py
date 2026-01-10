from ninja import Schema


class KafkaMessage(Schema):
    topic: str
    message: str
    key: str


class KafkaResponse(Schema):
    status: str
    message: str
    topic: str | None = None
    key: str | None = None
    error: str | None = None

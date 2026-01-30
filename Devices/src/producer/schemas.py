from ninja import Schema


class CommandSchema(Schema):
    device_uuid: str
    command: str


class KafkaMessage(Schema):
    topic: str
    key: str
    value: CommandSchema


class KafkaResponse(Schema):
    status: str
    message: str
    topic: str | None = None
    key: str | None = None
    error: str | None = None

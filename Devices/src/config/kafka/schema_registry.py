from typing import Any
from fastavro import parse_schema, validate

from config.settings import logger


class SchemaRegistryClient:

    COMMANDS_SCHEMA = {
        "type": "record",
        "name": "Command",
        "fields": [
            {"name": "device_uuid", "type": "string"},
            {"name": "command", "type": "string"}
        ]
    }

    def validate_command(
        self,
        message: dict,
    ) -> Any:

        try:
            parsed_schema = parse_schema(self.COMMANDS_SCHEMA)
            validate(message, parsed_schema)
            return parsed_schema
        except Exception as e:
            logger.error(f"Ошибка валидации: {e}")
            return None

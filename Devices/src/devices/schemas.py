from ninja import ModelSchema

from .choices import DevicesLocationChoices, DevicesProtocolChoices, DevicesTypeChoices
from .models import Devices


class DevicesResponse(ModelSchema):
    """Схема ответа для устройств."""

    class Meta:
        model = Devices
        fields = "__all__"


class DevicesCreateRequest(ModelSchema):
    """Схема для создания устройства."""

    type: DevicesTypeChoices
    location: DevicesLocationChoices
    protocol: DevicesProtocolChoices

    class Meta:
        model = Devices
        fields = ["name", "type", "location", "version", "protocol", "user_uuid", "description"]
        fields_optional = ["description"]


class DevicesUpdateRequest(ModelSchema):
    """Схема запроса для обновления полей устройства."""

    type: DevicesTypeChoices | None = None
    location: DevicesLocationChoices | None = None
    protocol: DevicesProtocolChoices | None = None

    class Meta:
        model = Devices
        fields = ["name", "type", "location", "version", "protocol", "user_uuid", "description"]
        fields_optional = "__all__"

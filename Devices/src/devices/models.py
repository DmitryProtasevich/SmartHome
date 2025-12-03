from django.db import models

from .choices import DevicesLocationChoices, DevicesProtocolChoices, DevicesTypeChoices
from .constants import Constants


class Devices(models.Model):
    """Устройства."""

    name = models.CharField(
        "Название",
        max_length=Constants.MAX_NAME_LENGTH,
    )
    type = models.CharField(
        "Тип устройства (Например: климатическое, освещение).",
        max_length=Constants.MAX_TYPE_LENGTH,
        choices=DevicesTypeChoices.choices,
    )
    location = models.CharField(
        "Местоположение устройства (Например: ванная, гостинная).",
        max_length=Constants.MAX_LOCATION_LENGTH,
        choices=DevicesLocationChoices.choices,
    )
    version = models.CharField(
        "Версия устройства (Например: LG Evo Max).",
        max_length=Constants.MAX_VERSION_LENGTH,
    )
    protocol = models.CharField(
        "Протокол связи с устройством (Например: Wifi).",
        max_length=Constants.MAX_PROTOCOL_LENGTH,
        choices=DevicesProtocolChoices.choices,
    )
    created_at = models.DateTimeField(
        "Дата создания.",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        "Дата обновления.",
        auto_now=True,
    )
    user_uuid = models.UUIDField(
        "UUID Пользователя Keycloak",
        db_index=True,
    )
    description = models.TextField(
        "Описание.",
        null=True,
        blank=True,
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=["name", "version"],
                name="unique_name_version",
            ),
        )
        verbose_name = "устройство"
        verbose_name_plural = "Устройства"

    def __str__(self):
        if len(self.name) > Constants.MAX_TITLE_LENGTH:
            return f"{self.name[:Constants.MAX_TITLE_LENGTH]}..."
        return self.name

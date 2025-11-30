from django.db import models


class DevicesTypeChoices(models.TextChoices):
    CLIMATE = "climate", "Climate"
    LIGHT = "light", "Light"
    CAMERA = "camera", "Camera"
    THERMO = "thermo", "Thermo"
    SENSOR = "sensor", "Sensor"
    SWITCH = "switch", "Switch"
    VACUUM = "vacuum", "Vacuum"


class DevicesLocationChoices(models.TextChoices):
    LIVING_ROOM = "living_room", "Living room"
    BEDROOM = "bedroom", "Bedroom"
    KITCHEN = "kitchen", "Kitchen"
    HALLWAY = "hallway", "Hallway"
    BATHROOM = "bathroom", "Bathroom"
    OUTDOOR = "outdoor", "Outdoor"


class DevicesProtocolChoices(models.TextChoices):
    WIFI = "wifi", "Wifi"
    ZIGBEE = "zigbee", "Zig Bee"

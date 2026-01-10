from ninja import NinjaAPI

from devices.api import devices_router
from internal.api import internal_router
from producer.api import producer_router

api = NinjaAPI(
    title="SmartHome API",
    version="1.0.0",
)

api.add_router("/devices", devices_router)
api.add_router("/internal", internal_router)
api.add_router("/producer", producer_router)

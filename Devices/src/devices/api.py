from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.responses import Response
from ninja.pagination import paginate, PageNumberPagination

from .models import Devices
from .schemas import DevicesCreateRequest, DevicesResponse, DevicesUpdateRequest

devices_router = Router()


@devices_router.get(
    "",
    tags=["devices"],
    summary="Получить список устройств.",
    response={200: list[DevicesResponse]}
)
@paginate(PageNumberPagination)
def get_devices(
    request,
) -> Response:
    return Devices.objects.all()


@devices_router.post(
    "",
    tags=["devices"],
    summary="Добавить устройство.",
    response={201: DevicesResponse}
)
def create_device(
    request,
    request_data: DevicesCreateRequest,
) -> Response:
    return Devices.objects.create(**request_data.dict())


@devices_router.get(
    "/{id}",
    tags=["devices"],
    summary="Получить информацию о устройстве.",
    response={200: DevicesResponse}
)
def get_device(
    request,
    id: int,
) -> Response:
    return get_object_or_404(Devices, id=id)


@devices_router.patch(
    "/{id}",
    tags=["devices"],
    summary="Обновить информацию о устройстве.",
    response={200: DevicesResponse}
)
def update_device(
    request,
    id: int,
    request_data: DevicesUpdateRequest,
) -> Response:
    Devices.objects.filter(id=id).update(**request_data.dict(exclude_unset=True))
    return get_object_or_404(Devices, id=id)


@devices_router.delete(
    "/{id}",
    tags=["devices"],
    summary="Удалить устройство.",
    response={204: None},
)
def delete_device(
    request,
    id: int,
):
    get_object_or_404(Devices, id=id).delete()
    return Response(status=204)

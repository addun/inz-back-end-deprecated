from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline

from machinery.models import Device, MeasuringCapability


class DeviceInline(GenericStackedInline):
    model = Device
    extra = 1
    max_num = 1
    min_num = 1

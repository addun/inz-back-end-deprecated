from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline

from machinery.models import Device, MeasuringCapability


class DeviceInline(GenericStackedInline):
    model = Device
    extra = 0
    max_num = 1
    min_num = 1


class MeasuringCapabilityInline(GenericTabularInline):
    model = MeasuringCapability
    extra = 0
    max_num = 1

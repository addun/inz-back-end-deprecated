from django.contrib.contenttypes.admin import GenericTabularInline

from machinery.models import Device, MeasuringCapability


class DeviceInline(GenericTabularInline):
    model = Device
    extra = 0


class MeasuringCapabilityInline(GenericTabularInline):
    model = MeasuringCapability
    extra = 0

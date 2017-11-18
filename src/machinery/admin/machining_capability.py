from django.contrib.contenttypes.admin import GenericTabularInline

from machinery.models import MachiningCapability


class MachiningCapabilityInline(GenericTabularInline):
    model = MachiningCapability
    extra = 0
    min_num = 1

from django.contrib.contenttypes.admin import GenericStackedInline

from machinery.models import MachiningCapability


class MachiningCapabilityInline(GenericStackedInline):
    model = MachiningCapability
    extra = 0
    min_num = 1

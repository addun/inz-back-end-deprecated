from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from machinery.models import MachiningCapability
from machinery.models.machining_capability import MachiningSize


class MachineSizeInline(admin.TabularInline):
    model = MachiningSize
    extra = 0


@admin.register(MachiningCapability)
class MachiningCapabilityAdmin(admin.ModelAdmin):
    inlines = [
        MachineSizeInline
    ]


class MachiningCapabilityInline(GenericTabularInline):
    model = MachiningCapability
    extra = 0
    min_num = 1
    show_change_link = True

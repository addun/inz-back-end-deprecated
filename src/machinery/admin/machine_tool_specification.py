from django.contrib import admin

from machinery.admin.machine_tool_element import MachineToolElementInline
from machinery.admin.machining_capability import MachiningCapabilityInline
from machinery.admin.nc_controller import NcControllerInline
from machinery.admin.others import MeasuringCapabilityInline, DeviceInline
from machinery.models import MachineToolSpecification, Installation, Locator
from machinery.models.machine_tool_specification import MachineKinematicAssociation


class InstallationInline(admin.StackedInline):
    model = Installation
    show_change_link = True


class LocatorInline(admin.StackedInline):
    model = Locator


@admin.register(MachineToolSpecification)
class MachineToolSpecificationAdmin(admin.ModelAdmin):
    inlines = [
        InstallationInline,
        MeasuringCapabilityInline,
        MachiningCapabilityInline,
        DeviceInline,
        MachineToolElementInline,
        LocatorInline,
        NcControllerInline
    ]


class MachineToolSpecificationInline(admin.StackedInline):
    model = MachineToolSpecification
    show_change_link = True


@admin.register(MachineKinematicAssociation)
class MachineKinematicAssociationAdmin(admin.ModelAdmin):
    inlines = [
        MachineToolSpecificationInline
    ]

from django.contrib import admin

from machinery.admin import InstallationInline
from machinery.admin.environmental_evaluation import EnvironmentalEvaluationInline
from machinery.admin.machining_capability import MachiningCapabilityInline
from machinery.admin.nc_controller import NcControllerInline
from machinery.admin.others import MeasuringCapabilityInline, DeviceInline
from machinery.models import MachineToolSpecification, Locator
from machinery.models.machine_tool_specification import MachineKinematicAssociation


class LocatorInline(admin.StackedInline):
    model = Locator


@admin.register(MachineToolSpecification)
class MachineToolSpecificationAdmin(admin.ModelAdmin):
    inlines = [
        DeviceInline,
        MachiningCapabilityInline,
        MeasuringCapabilityInline,
        LocatorInline,
        InstallationInline,
        NcControllerInline,
        EnvironmentalEvaluationInline
    ]


@admin.register(MachineKinematicAssociation)
class MachineKinematicAssociationAdmin(admin.ModelAdmin):
    pass

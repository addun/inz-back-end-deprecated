from django.contrib import admin

from machinery.admin import InstallationInline
from machinery.admin.environmental_evaluation import EnvironmentalEvaluationInline
from machinery.admin.machine_tool_element import MachineToolElementInline
from machinery.admin.machining_capability import MachiningCapabilityInline
from machinery.admin.nc_controller import NcControllerInline
from machinery.admin.others import MeasuringCapabilityInline, DeviceInline
from machinery.models import MachineToolSpecification
from machinery.models.machine_tool_specification import MachineKinematicAssociation


@admin.register(MachineToolSpecification)
class MachineToolSpecificationAdmin(admin.ModelAdmin):
    inlines = [
        DeviceInline,
        MachiningCapabilityInline,
        MeasuringCapabilityInline,
        InstallationInline,
        NcControllerInline,
        EnvironmentalEvaluationInline,
        MachineToolElementInline
    ]


@admin.register(MachineKinematicAssociation)
class MachineKinematicAssociationAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin

from machinery.admin.machining_capability import MachiningCapabilityInline
from machinery.admin.others import MeasuringCapabilityInline
from machinery.models import SpindleCapability, MachineToolRequirement, \
    RangeOfMotion, WorkplanPhysicalResourceAssociation, ProjectPhysicalResourceAssociation


class SpindleCapabilityInline(admin.TabularInline):
    model = SpindleCapability
    extra = 0


@admin.register(MachineToolRequirement)
class MachineToolRequirementAdmin(admin.ModelAdmin):
    inlines = [
        MachiningCapabilityInline,
        SpindleCapabilityInline,
        MeasuringCapabilityInline
    ]


class RangeOfMotionInline(admin.TabularInline):
    model = RangeOfMotion
    extra = 0
    min_num = 1


@admin.register(WorkplanPhysicalResourceAssociation)
class WorkplanPhysicalResourceAssociation(admin.ModelAdmin):
    pass


@admin.register(ProjectPhysicalResourceAssociation)
class ProjectPhysicalResourceAssociationAdmin(admin.ModelAdmin):
    pass

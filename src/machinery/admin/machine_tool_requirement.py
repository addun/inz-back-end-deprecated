from django.contrib import admin

from machinery.admin.machining_capability import MachiningCapabilityInline
from machinery.admin.others import MeasuringCapabilityInline
from machinery.models import SpindleCapability, AxisCapability, PositioningCapability, MachineToolRequirement, \
    RangeOfMotion, WorkplanPhysicalResourceAssociation, ProjectPhysicalResourceAssociation


class SpindleCapabilityInline(admin.TabularInline):
    model = SpindleCapability
    extra = 0


class AxisCapabilityInline(admin.TabularInline):
    model = AxisCapability
    extra = 0


class PositioningCapabilityInline(admin.TabularInline):
    model = PositioningCapability
    extra = 0
    show_change_link = True


@admin.register(MachineToolRequirement)
class MachineToolRequirementAdmin(admin.ModelAdmin):
    inlines = [
        MachiningCapabilityInline,
        SpindleCapabilityInline,
        PositioningCapabilityInline,
        AxisCapabilityInline,
        MeasuringCapabilityInline
    ]


class RangeOfMotionInline(admin.TabularInline):
    model = RangeOfMotion
    extra = 0
    min_num = 1


@admin.register(PositioningCapability)
class PositioningCapabilityAdmin(admin.ModelAdmin):
    inlines = [
        RangeOfMotionInline
    ]


@admin.register(WorkplanPhysicalResourceAssociation)
class WorkplanPhysicalResourceAssociation(admin.ModelAdmin):
    pass


@admin.register(ProjectPhysicalResourceAssociation)
class ProjectPhysicalResourceAssociationAdmin(admin.ModelAdmin):
    pass

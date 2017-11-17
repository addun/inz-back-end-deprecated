from django.contrib import admin

from machinery.models import *


class ProjectPhysicalResourceAssociationInline(admin.StackedInline):
    model = ProjectPhysicalResourceAssociation
    extra = 1


class WorkplanPhysicalResourceAssociationInline(admin.StackedInline):
    model = WorkplanPhysicalResourceAssociation
    extra = 1


class SpindleCapabilityInline(admin.TabularInline):
    model = SpindleCapability
    extra = 1


class AxisCapabilityInline(admin.StackedInline):
    model = AxisCapability
    extra = 1


class PositioningCapabilityInline(admin.TabularInline):
    model = PositioningCapability
    extra = 1
    show_change_link = True


class RangeOfMotionStackedInline(admin.TabularInline):
    model = RangeOfMotion
    extra = 0


@admin.register(PositioningCapability)
class RangeOfMotionAdmin(admin.ModelAdmin):
    inlines = [
        RangeOfMotionStackedInline
    ]


@admin.register(MachineToolRequirement)
class MachineToolRequirementAdmin(admin.ModelAdmin):
    inlines = [
        ProjectPhysicalResourceAssociationInline,
        WorkplanPhysicalResourceAssociationInline,
        SpindleCapabilityInline,
        AxisCapabilityInline,
        PositioningCapabilityInline,
    ]

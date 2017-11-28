from django.db import models

from machinery import schemas
from machinery.models.others import MachineTool, MeasuringCapability


class AxisCapability(models.Model):
    number_of_axes = schemas.Measure.count(null=True, blank=True)
    number_of_simultaneous_axes = schemas.Measure.count(null=True, blank=True)

    class Meta:
        abstract = True


class PositioningCapability(models.Model):
    maximum_displacement_error_of_linear_axis = schemas.Measure.length(null=True, blank=True)
    maximum_repeatability_error_of_linear_axis = schemas.Measure.length(null=True, blank=True)

    class Meta:
        abstract = True


class MachineToolRequirement(MachineTool, AxisCapability, PositioningCapability, MeasuringCapability):
    number_of_tools_in_tool_magazine = schemas.Measure.count(null=True, blank=True)
    automatically_pallet_changeable = schemas.Base.boolean()


class ProjectPhysicalResourceAssociation(models.Model):
    machine_tool_requirement = models.ForeignKey(MachineToolRequirement, on_delete=models.CASCADE)
    project_of_resource = schemas.Machining.project()


class WorkplanPhysicalResourceAssociation(models.Model):
    machine_tool_requirement = models.ForeignKey(MachineToolRequirement, on_delete=models.CASCADE)
    workplan_of_resource = schemas.Machining.workplan()


class SpindleCapability(models.Model):
    machine_tool_requirement = models.ForeignKey(MachineToolRequirement, on_delete=models.CASCADE)
    spindle_name = schemas.SupportResource.label()
    spindle_power = schemas.Measure.power()
    maximum_drive_speed = schemas.Measure.count()


class RangeOfMotion(models.Model):
    positioning_capability = models.ForeignKey(MachineToolRequirement, on_delete=models.CASCADE)
    axis_name = schemas.SupportResource.label()
    motion_range = schemas.Select.angle_or_length()

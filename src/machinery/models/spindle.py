from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from machinery import schemas
from machinery.models import MachineToolElement
from machinery.models.element_capability import ElementCapability


class SpindleAbstract(ElementCapability):
    spindle_power = schemas.Measure.power()
    spindle_name = schemas.SupportResource.label()
    spindle_manufacturer = schemas.SupportResource.label(null=True, blank=True)
    manufacturer_model_designation = schemas.SupportResource.label(null=True, blank=True)

    class Meta:
        abstract = True


class Spindle(SpindleAbstract):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE, related_name='spindle')


class SpindleRange(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    minimum_drive_speed = schemas.Machining.rot_speed()
    maximum_drive_speed = schemas.Machining.rot_speed()
    minimum_drive_torque = schemas.Measure.torque()
    maximum_drive_torque = schemas.Measure.torque()


class ToolSpindle(SpindleAbstract):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE, related_name='toolspindle')
    spindle_tool_holder_style_designation = schemas.SupportResource.label()
    coolant_through_spindle = schemas.Base.boolean()

    class Meta:
        abstract = True


class TaperedSpindle(ToolSpindle):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE,
                                             related_name='taperedspindle')
    spindle_taper_designation = schemas.SupportResource.label()


class StraightSpindle(ToolSpindle):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE,
                                             related_name='straightspindle')
    spindle_bore_depth = schemas.Measure.length()
    spindle_bore_diameter = schemas.Measure.length()


class ThreadedSpindle(ToolSpindle):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE,
                                             related_name='threadedspindle')
    spindle_thread_diameter = schemas.Measure.length()
    spindle_thread_pitch = schemas.Measure.length()
    spindle_thread_form = schemas.SupportResource.label()


class WorkSpindle(SpindleAbstract):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE, related_name='workspindle')
    spindle_nose_designation = schemas.SupportResource.label()
    spindle_bore_diameter = schemas.Measure.length()
    round_bar_stock_diameter = schemas.Measure.length(null=True, blank=True)
    through_hole_diameter = schemas.Measure.length(null=True, blank=True)
    hex_bar_stock_capacity = schemas.Base.real(null=True, blank=True)

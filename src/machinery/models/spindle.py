from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from machinery import schemas
from machinery.models.element_capability import ElementCapability, Chuck


class Spindle(ElementCapability):
    spindle_power = schemas.Measure.power()
    spindle_name = schemas.SupportResource.label()
    spindle_manufacturer = schemas.SupportResource.label(null=True, blank=True)
    manufacturer_model_designation = schemas.SupportResource.label(null=True, blank=True)


class WorkSpindle(Spindle):
    spindle_nose_designation = schemas.SupportResource.label()
    spindle_bore_diameter = schemas.Measure.length()
    round_bar_stock_diameter = schemas.Measure.length(null=True, blank=True)
    through_hole_diameter = schemas.Measure.length(null=True, blank=True)
    hex_bar_stock_capacity = schemas.Base.real(null=True, blank=True)


class ToolSpindle(Spindle):
    spindle_tool_holder_style_designation = schemas.SupportResource.label()
    coolant_through_spindle = schemas.Base.boolean()

    class Meta:
        abstract = True


class TaperedSpindle(ToolSpindle):
    spindle_taper_designation = schemas.SupportResource.label()


class StraightSpindle(ToolSpindle):
    spindle_bore_depth = schemas.Measure.length()
    spindle_bore_diameter = schemas.Measure.length()


class ThreadedSpindle(ToolSpindle):
    spindle_thread_diameter = schemas.Measure.length()
    spindle_thread_pspindle_thread_formitch = schemas.Measure.length()
    spindle_thread_form = schemas.SupportResource.label()


class SpindleRange(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    minimum_drive_speed = schemas.Machining.rot_speed()
    maximum_drive_speed = schemas.Machining.rot_speed()
    minimum_drive_torque = schemas.Other.torque_measure()
    maximum_drive_torque = schemas.Other.torque_measure()

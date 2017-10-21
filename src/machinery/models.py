# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from . import schemas


# Create your models here.


class MachineTool(models.Model):
    """
    This entity is a supertype of machine_tool_specification and machine_tool_requirements.

    description : This attribute specifies the word, or group of words, that describe the machine tool needed.
    """
    description = schemas.SupportResource.text()

    class Meta:
        db_table = 'machine_tool'


class MachineToolRequirements(MachineTool):
    """
    5,1
    This entity describes requirements for the machine tool.

    number_of_tools_in_tool_magazine : This attribute specifies the number of tools in the tool magazine.
    machining                        : This attribute specifies the machining capability of the machine tool.
    spindles                         : This attribute specifies the spindle capability of the machine tool.
    positioning                      : This attribute specifies the positioning capability of the machine tool.
    axis                             : This attribute specifies the axis capability of the machine tool.
    touch_probing                    : This attribute specifies the measuring capability of the machine tool. automatically_pallet_changeable: This attribute specifies whether the machine tool has an automatic pallet changer.
    """
    number_of_tools_in_tool_magazine = schemas.Measure.count_measure()
    machining = models.ManyToManyField('MachiningCapability')
    # spindles
    positioning = models.OneToOneField('PositioningCapability', blank=True, null=True)
    axis = models.OneToOneField('AxisCapability', on_delete=models.CASCADE, blank=True, null=True)
    touch_probing = models.OneToOneField('MeasuringCapability', on_delete=models.CASCADE, blank=True, null=True)
    automatically_pallet_changeable = models.BooleanField()


class MachiningCapability(models.Model):
    machining_capability_profile = (
        ('BORING', 'BORING_CAPABILITY'),
        ('DRILLING', 'DRILLING_CAPABILITY'),
        ('GUNDRILL', 'GUNDRILL_CAPABILITY'),
        ('MILLING', 'MILLING_CAPABILITY'),
        ('TURNING', 'TURNING_CAPABILITY')
    )

    capability = models.CharField(choices=machining_capability_profile, max_length=15)
    machining_accuracy = schemas.SupportResource.text_optional()
    description = schemas.SupportResource.text_optional()
    machining_size = models.OneToOneField('MachineSize', null=True, blank=True)

    class Meta:
        db_table = 'machining_capability'


class SpindleCapability(models.Model):
    machine_tool_requirements_id = models.ForeignKey('MachineToolRequirements')
    spindle_name = schemas.SupportResource.label()
    spindle_power = schemas.Measure.power_measure()
    maximum_drive_speed = schemas.Machining.rot_speed_measure()

    class Meta:
        db_table = 'spindle_capability'


class PositioningCapability(models.Model):
    """
    This entity describes the positioning capability of the machine tool.

    maximum_range_of_motion                     : This attribute specifies the maximum programmable axis travel of each linear axis.
    maximum_displacement_error_of_linear_axis   : This attribute specifies the maximum displacement error of axis movements.
    maximum_repeatability_error_of_linear_axis  : This attribute specifies the maximum repeatability error of axis movements.
    """
    maximum_range_of_motion = models.OneToOneField('RangeOfMotion', on_delete=models.CASCADE)
    maximum_displacement_error_of_linear_axis = schemas.Measure.length_measure()
    maximum_repeatability_error_of_linear_axis = schemas.Measure.length_measure()

    class Meta:
        db_table = 'positioning_capability'


class RangeOfMotion(models.Model):
    """
    This entity describes the properties of a range of motion.

    axis_name       : This attribute specifies the name of the axis.
    motion_range    : This attribute specifies the range of motion.
    """
    axis_name = schemas.SupportResource.label()
    motion_range = models.TextField()  # ToDo: angle_or_length (class AngleOrLength)

    class Meta:
        db_table = 'Rangeo_of_motion'


# class AngleOrLength(models.Model):
#     pass


class AxisCapability(models.Model):
    """
    This entity describes the specification of machine tool axes.

    number_of_axes              : This attribute specifies the number of axes.
    number_of_simultaneous_axes : This attribute specifies the number of axes controlled by NC controller simultaneously. The number of simultaneous axes controlled must not be greater than the total number of axes.
    """
    number_of_axes = schemas.Measure.count_measure()
    number_of_simultaneous_axes = schemas.Measure.count_measure()

    class Meta:
        db_table = 'axis_capability'


class MeasuringCapability(models.Model):
    """
    4,2
    This entity describes the measuring capability of the machine tool.

    measuring_accuracy  : This attribute specifies the accuracy of the measurement on the machine tool.
    description         : This attribute specifies the word or group of words used to provide information about the measuring capability.
    """
    measuring_accuracy = schemas.SupportResource.text()
    description = schemas.SupportResource.text_optional()

    class Meta:
        db_table = 'measuring_capability'


# class Locator(models.Model):
#     """
#     This entity describes the location and ownership information of the machine within a company.
#     The exact content of locator is company specific.
#
#     business_unit   : This attribute specifies the facility code of the business unit within the company to which the machine belongs.
#     plant_location  : This attribute specifies the geographic location of the plant where the machine resides.
#     building        : This attribute specifies the designation of the building in which the machine is installed.
#     cell            : This attribute specifies the description of the actual location of the cell.
#     """
#
#     business_unit = fields.get_label()
#     plant_location = fields.get_label()
#     building = fields.get_label()
#     cell = fields.get_label()
#     test = fields.get_label()
#
#
class MachineSize(models.Model):
    """
    This entity describes the size of the workpiece which can be machined with the machine tool with reference to the axis directions of a machine tool.

    description : This attribute specifies the word or group of words used to provide information about the machining size.
    x           : This attribute specifies the length of the workpiece which can be machined with the machine tool.
    y           : This attribute specifies the width of the workpiece which can be machined with the machine tool.
    z           : This attribute specifies the height of the workpiece which can be machined with the machine tool.
    """
    description = schemas.SupportResource.text_optional()
    x = schemas.Measure.length_measure()
    y = schemas.Measure.length_measure()
    z = schemas.Measure.length_measure()

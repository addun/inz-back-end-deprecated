# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from machinery import schemas


class NcController(models.Model):
    controller_model = schemas.SupportResource.label()
    controller_manufacturer = schemas.SupportResource.label()
    units = schemas.Enumerations.units()
    maximum_number_of_simultaneous_control_axes = schemas.Measure.count_measure()
    maximum_total_number_of_control_feed_axes = schemas.Measure.count_measure()
    maximum_total_number_of_control_spindles = schemas.Measure.count_measure()
    minimum_linear_increment = schemas.Measure.length_measure()
    minimum_angle_increment = schemas.Measure.plane_angle_measure()
    maximum_number_of_multi_channel_control = schemas.Measure.count_measure()
    look_ahead = models.IntegerField(null=True, blank=True)
    adaptive_control = schemas.SupportResource.text(blank=True, null=True)
    miscellaneous_controller_functions = schemas.SupportResource.text(blank=True, null=True)
    program_memory_size = models.IntegerField(blank=True, null=True)
    time_sampling = schemas.Measure.time_measure(blank=True, null=True)
    clock_frequency = schemas.Measure.count_measure(blank=True, null=True)


class ToolCompensationFunction(models.Model):
    nc_controller = models.ForeignKey(NcController, on_delete=models.CASCADE)
    tool_compensation_function = schemas.Measure.count_measure()


class CycleFunction(models.Model):
    nc_controller = models.ForeignKey(NcController, on_delete=models.CASCADE)
    cycle_function = schemas.SupportResource.text()


class InterpolationFunction(models.Model):
    nc_controller = models.ForeignKey(NcController, on_delete=models.CASCADE)
    interpolation_function = schemas.SupportResource.text()


class CuttingFeedRateOverride(models.Model):
    nc_controller = models.ForeignKey(NcController, on_delete=models.CASCADE)
    cutting_feed_rate_override = schemas.Measure.ratio_measure()


class RapidTraverseOverride(models.Model):
    nc_controller = models.ForeignKey(NcController, on_delete=models.CASCADE)
    rapid_traverse_override = schemas.Measure.ratio_measure()

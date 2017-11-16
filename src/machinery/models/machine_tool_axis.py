from django.db import models

from machinery import schemas
from machinery.models.element_capability import ElementCapability


class MachineToolAxis(ElementCapability):
    axis_name = schemas.SupportResource.label()


class LinearAxis(MachineToolAxis):
    minimum_range_of_motion = schemas.Measure.length()
    maximum_range_of_motion = schemas.Measure.length()
    displacement_error = schemas.Measure.length()
    repeatability_error = schemas.Measure.length()
    rapid_traverse_feed_rate = schemas.Measure.velocity()
    minimum_cutting_feed_rate = schemas.Measure.velocity()
    maximum_cutting_feed_rate = schemas.Measure.velocity()
    maximum_acceleration = schemas.Measure.velocity(null=True, blank=True)
    maximum_deceleration = schemas.Measure.velocity(null=True, blank=True)
    maximum_jerk = schemas.Other.jerk_measure(null=True, blank=True)

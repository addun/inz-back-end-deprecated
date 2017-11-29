from django.db import models

from machinery import schemas
from machinery.models import MachineToolElement
from machinery.models.element_capability import ElementCapability


class MachineToolAxisAbstract(ElementCapability):
    axis_name = schemas.SupportResource.label()

    class Meta:
        abstract = True


class MachineToolAxis(MachineToolAxisAbstract):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE, related_name="machinetoolaxis")
    pass


class LinearAxis(MachineToolAxisAbstract):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE, related_name="linearaxis")
    minimum_range_of_motion = schemas.Measure.length()
    maximum_range_of_motion = schemas.Measure.length()
    displacement_error = schemas.Measure.length()
    repeatability_error = schemas.Measure.length()
    rapid_traverse_feed_rate = schemas.Measure.velocity()
    minimum_cutting_feed_rate = schemas.Measure.velocity()
    maximum_cutting_feed_rate = schemas.Measure.velocity()
    maximum_acceleration = schemas.Measure.acceleration(null=True, blank=True)
    maximum_deceleration = schemas.Measure.acceleration(null=True, blank=True)
    maximum_jerk = schemas.Measure.jerk(null=True, blank=True)

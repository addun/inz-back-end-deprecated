from django.db import models

from machinery import schemas
from machinery.models import MachineToolAxisAbstract, MachineToolElement


class RotaryAxis(MachineToolAxisAbstract):
    displacement_angle_error = schemas.Measure.plane_angle()
    repeatability_angle_error = schemas.Measure.plane_angle()
    rapid_traverse_rotation_feed_rate = schemas.Machining.rot_speed()
    minimum_cutting_rotation_feed_rate = schemas.Machining.rot_speed()
    maximum_cutting_rotation_feed_rate = schemas.Machining.rot_speed()
    maximum_rotation_deceleration = schemas.Measure.rot_acceleration(null=True, blank=True)
    maximum_rotation_acceleration = schemas.Measure.rot_acceleration(null=True, blank=True)
    maximum_rotation_jerk = schemas.Measure.rot_jerk(null=True, blank=True)

    class Meta:
        abstract = True


class ContinuousRotary(RotaryAxis):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE,
                                             related_name='continuousrotary')
    pass


class Indexing(RotaryAxis):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE, related_name='indexing')
    index_increment = schemas.Measure.plane_angle()


class LimitedSwing(RotaryAxis):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE, related_name='limitedswing')
    minimum_angle_of_motion = schemas.Measure.plane_angle()
    maximum_angle_of_motion = schemas.Measure.plane_angle()
    axis_travel_limit = schemas.Base.boolean()

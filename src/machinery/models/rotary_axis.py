from django.db import models

from machinery import schemas


class RotaryAxis(models.Model):
    displacement_angle_error = schemas.Measure.plane_angle()
    repeatability_angle_error = schemas.Measure.plane_angle()
    rapid_traverse_rotation_feed_rate = schemas.Machining.rot_speed()
    minimum_cutting_rotation_feed_rate = schemas.Machining.rot_speed()
    maximum_cutting_rotation_feed_rate = schemas.Machining.rot_speed()
    maximum_rotation_deceleration = schemas.Other.rot_acceleration_measure(null=True, blank=True)
    maximum_rotation_acceleration = schemas.Other.rot_acceleration_measure(null=True, blank=True)
    maximum_rotation_jerk = schemas.Other.rot_jerk_measure(null=True, blank=True)

    class Meta:
        abstract = True


class ContinuousRotary(RotaryAxis):
    pass


class Indexing(RotaryAxis):
    index_increment = schemas.Measure.plane_angle()


class LimitedSwing(RotaryAxis):
    minimum_angle_of_motion = schemas.Measure.plane_angle()
    maximum_angle_of_motion = schemas.Measure.plane_angle()
    axis_travel_limit = schemas.Measure.plane_angle()

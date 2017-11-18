from machinery import schemas
from machinery.models import MachineToolAxis


class RotaryAxis(MachineToolAxis):
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
    pass


class Indexing(RotaryAxis):
    index_increment = schemas.Measure.plane_angle()


class LimitedSwing(RotaryAxis):
    minimum_angle_of_motion = schemas.Measure.plane_angle()
    maximum_angle_of_motion = schemas.Measure.plane_angle()
    axis_travel_limit = schemas.Base.boolean()

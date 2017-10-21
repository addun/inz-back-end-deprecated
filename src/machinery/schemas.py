from django.db import models


class DateTime(models.Model):
    calendar_date = models.DateField()

    class Meta:
        abstract = True


class Geometry(models.Model):
    axis2_placement_3d = models.CharField(max_length=15)

    class Meta:
        abstract = True


class KinematicStructure(models.Model):
    cylindrical_pair = models.CharField(max_length=15)
    cylindrical_pair_range = models.CharField(max_length=15)
    kinematic_joint = models.CharField(max_length=15)
    kinematic_link = models.CharField(max_length=15)
    kinematic_link_representation = models.CharField(max_length=15)
    kinematic_link_representation_association = models.CharField(max_length=15)
    kinematic_link_representation_relation = models.CharField(max_length=15)
    kinematic_pair = models.CharField(max_length=15)
    kinematic_property_definition = models.CharField(max_length=15)
    kinematic_structure = models.CharField(max_length=15)
    mechanism = models.CharField(max_length=15)
    pair_actuator = models.CharField(max_length=15)
    prismatic_pair = models.CharField(max_length=15)
    prismatic_pair_range = models.CharField(max_length=15)
    revolute_pair = models.CharField(max_length=15)
    revolute_pair_range = models.CharField(max_length=15)
    rotational_range_measure = models.CharField(max_length=15)
    simple_pair_range = models.CharField(max_length=15)
    spherical_pair = models.CharField(max_length=15)
    spherical_pair_range = models.CharField(max_length=15)
    su_parameters = models.CharField(max_length=15)
    translational_range_measure = models.CharField(max_length=15)
    unlimited_range = models.CharField(max_length=15)

    class Meta:
        abstract = True


class Machining(models.Model):
    project = models.CharField(max_length=15)
    rot_speed_measure = models.CharField(max_length=15)
    workplan = models.CharField(max_length=15)

    class Meta:
        abstract = True


class Measure(models.Model):
    acceleration_measure = models.CharField(max_length=15)
    count_measure = models.CharField(max_length=15)
    electric_current_measure = models.CharField(max_length=15)
    length_measure = models.CharField(max_length=15)
    plane_angle_measure = models.CharField(max_length=15)
    mass_measure = models.CharField(max_length=15)
    power_measure = models.CharField(max_length=15)
    pressure_measure = models.CharField(max_length=15)
    ratio_measure = models.CharField(max_length=15)
    time_measure = models.CharField(max_length=15)
    velocity_measure = models.CharField(max_length=15)
    volume_measur = models.CharField(max_length=15)

    class Meta:
        abstract = True


class ProductDefinition(models.Model):
    product_definition = models.CharField(max_length=15)

    class Meta:
        abstract = True


class ProductPropertyDefinition(models.Model):
    characterized_definition = models.CharField(max_length=15)
    characterized_object = models.CharField(max_length=15)
    characterized_product_definition = models.CharField(max_length=15)

    class Meta:
        abstract = True


class ProductPropertyRepresentation(models.Model):
    shape_representation = models.CharField(max_length=15)

    class Meta:
        abstract = True


class SupportResource(models.Model):
    identifier = models.CharField(max_length=15)
    label = models.CharField(max_length=15)
    text = models.CharField(max_length=15)

    class Meta:
        abstract = True

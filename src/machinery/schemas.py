from django.db import models


class DateTime(models.Model):
    @staticmethod
    def calendar_date():
        return models.DateField()

    class Meta:
        abstract = True


class Geometry(models.Model):
    @staticmethod
    def axis2_placement_3d():
        return models.CharField(max_length=15)

    class Meta:
        abstract = True


class KinematicStructure(models.Model):
    @staticmethod
    def cylindrical_pair():
        return models.CharField(max_length=15)

    @staticmethod
    def cylindrical_pair_range():
        return models.CharField(max_length=15)

    @staticmethod
    def kinematic_joint():
        return models.CharField(max_length=15)

    @staticmethod
    def kinematic_link():
        return models.CharField(max_length=15)

    @staticmethod
    def kinematic_link_representation():
        return models.CharField(max_length=15)

    @staticmethod
    def kinematic_link_representation_association():
        return models.CharField(max_length=15)

    @staticmethod
    def kinematic_link_representation_relation():
        return models.CharField(max_length=15)

    @staticmethod
    def kinematic_pair():
        return models.CharField(max_length=15)

    @staticmethod
    def kinematic_property_definition():
        return models.CharField(max_length=15)

    @staticmethod
    def kinematic_structure():
        return models.CharField(max_length=15)

    @staticmethod
    def mechanism():
        return models.CharField(max_length=15)

    @staticmethod
    def pair_actuator():
        return models.CharField(max_length=15)

    @staticmethod
    def prismatic_pair():
        return models.CharField(max_length=15)

    @staticmethod
    def prismatic_pair_range():
        return models.CharField(max_length=15)

    @staticmethod
    def revolute_pair():
        return models.CharField(max_length=15)

    @staticmethod
    def revolute_pair_range():
        return models.CharField(max_length=15)

    @staticmethod
    def rotational_range_measure():
        return models.CharField(max_length=15)

    @staticmethod
    def simple_pair_range():
        return models.CharField(max_length=15)

    @staticmethod
    def spherical_pair():
        return models.CharField(max_length=15)

    @staticmethod
    def spherical_pair_range():
        return models.CharField(max_length=15)

    @staticmethod
    def su_parameters():
        return models.CharField(max_length=15)

    @staticmethod
    def translational_range_measure():
        return models.CharField(max_length=15)

    @staticmethod
    def unlimited_range():
        return models.CharField(max_length=15)

    class Meta:
        abstract = True


class Machining(models.Model):
    @staticmethod
    def project():
        return models.CharField(max_length=15)

    @staticmethod
    def rot_speed_measure():
        return models.CharField(max_length=15)

    @staticmethod
    def workplan():
        return models.CharField(max_length=15)

    class Meta:
        abstract = True


class Measure(models.Model):
    @staticmethod
    def acceleration_measure():
        return models.CharField(max_length=15)

    @staticmethod
    def count_measure():
        return models.CharField(max_length=15)

    @staticmethod
    def electric_current_measure():
        return models.CharField(max_length=15)

    @staticmethod
    def length_measure():
        return models.CharField(max_length=15)

    @staticmethod
    def plane_angle_measure():
        return models.CharField(max_length=15)

    @staticmethod
    def mass_measure():
        return models.CharField(max_length=15)

    @staticmethod
    def power_measure():
        return models.CharField(max_length=15)

    @staticmethod
    def pressure_measure():
        return models.CharField(max_length=15)

    @staticmethod
    def ratio_measure():
        return models.CharField(max_length=15)

    @staticmethod
    def time_measure():
        return models.CharField(max_length=15)

    @staticmethod
    def velocity_measure():
        return models.CharField(max_length=15)

    @staticmethod
    def volume_measur():
        return models.CharField(max_length=15)

    class Meta:
        abstract = True


class ProductDefinition(models.Model):
    @staticmethod
    def product_definition():
        return models.CharField(max_length=15)

    class Meta:
        abstract = True


class ProductPropertyDefinition(models.Model):
    @staticmethod
    def characterized_definition():
        return models.CharField(max_length=15)

    @staticmethod
    def characterized_object():
        return models.CharField(max_length=15)

    @staticmethod
    def characterized_product_definition():
        return models.CharField(max_length=15)

    class Meta:
        abstract = True


class ProductPropertyRepresentation(models.Model):
    @staticmethod
    def shape_representation():
        return models.CharField(max_length=15)

    class Meta:
        abstract = True


class SupportResource(models.Model):
    @staticmethod
    def identifier():
        return models.CharField(max_length=15)

    @staticmethod
    def label():
        return models.CharField(max_length=15)

    @staticmethod
    def text():
        return models.CharField(max_length=15)

    @staticmethod
    def text_optional():
        return models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        abstract = True

from django.db import models


class Base(models.Model):
    @staticmethod
    def real(**kwargs):
        return models.IntegerField(**kwargs)

    @staticmethod
    def integer(**kwargs):
        return models.IntegerField(**kwargs)

    @staticmethod
    def string(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    class Meta:
        abstract = True


class DateTime(models.Model):
    @staticmethod
    def calendar_date(**kwargs):
        return models.DateField(**kwargs)

    class Meta:
        abstract = True


class Geometry(models.Model):
    @staticmethod
    def axis2_placement_3d(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    class Meta:
        abstract = True


class KinematicStructure(models.Model):
    @staticmethod
    def cylindrical_pair(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def cylindrical_pair_range(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def kinematic_joint(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def kinematic_link(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def kinematic_link_representation(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def kinematic_link_representation_association(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def kinematic_link_representation_relation(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def kinematic_pair(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def kinematic_property_definition(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def kinematic_structure(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def mechanism(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def pair_actuator(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def prismatic_pair(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def prismatic_pair_range(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def revolute_pair(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def revolute_pair_range(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def rotational_range_measure(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def simple_pair_range(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def spherical_pair(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def spherical_pair_range(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def su_parameters(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def translational_range_measure(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def unlimited_range(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    class Meta:
        abstract = True


class Machining(models.Model):
    @staticmethod
    def project(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def rot_speed(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def workplan(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    class Meta:
        abstract = True


class Measure(models.Model):
    @staticmethod
    def acceleration(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def count(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def electric_current(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def length(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def plane_angle(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def mass(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def power(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def pressure(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def ratio(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def time(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def velocity(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def volume(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    class Meta:
        abstract = True


class ProductDefinition(models.Model):
    @staticmethod
    def product_definition(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    class Meta:
        abstract = True


class ProductPropertyDefinition(models.Model):
    @staticmethod
    def characterized_definition(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def characterized_object(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def characterized_product_definition(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    class Meta:
        abstract = True


class ProductPropertyRepresentation(models.Model):
    @staticmethod
    def shape_representation(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    class Meta:
        abstract = True


class SupportResource(models.Model):
    @staticmethod
    def identifier(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def label(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def text(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    class Meta:
        abstract = True


class Enumerations(models.Model):
    @staticmethod
    def units():
        UNITS_TYPE = (
            ('INCH', 'small'),
            ('INCH_AND_METRIC', 'inch and metric'),
            ('METRIC', 'metric'),
        )
        return models.CharField(max_length=25, choices=UNITS_TYPE)

    @staticmethod
    def interpolation():
        INTERPOLATION = (
            ('CIRCULAR', 'circular'),
            ('HELICAL', 'helical'),
            ('LINEAR', 'linear'),
            ('NURBS', 'nurbs'),
            ('OTHER', 'other'),
        )
        return models.CharField(max_length=25, choices=INTERPOLATION)

    @staticmethod
    def tool_compensation():
        TOOL_COMPENSATION = (
            ('TOOL_LENGTH', 'tool_length'),
            ('TOOL_RADIUS', 'tool_radius'),
        )
        return models.CharField(max_length=25, choices=TOOL_COMPENSATION)

    class Meta:
        abstract = True

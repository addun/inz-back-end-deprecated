from django.db import models


class Select(models.Model):
    @staticmethod
    def angle_or_length(**kwargs):
        return models.IntegerField(**kwargs)

    class Meta:
        abstract = True


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

    @staticmethod
    def boolean(**kwargs):
        return models.BooleanField(**kwargs)

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
    def units(**kwargs):
        UNITS_TYPE = (
            ('INCH', 'small'),
            ('INCH_AND_METRIC', 'inch and metric'),
            ('METRIC', 'metric'),
        )
        return models.CharField(max_length=25, choices=UNITS_TYPE, **kwargs)

    @staticmethod
    def pallet_storage_configuration(**kwargs):
        PALLET_STORAGE_CONFIGURATION = (
            ('CAROUSEL', 'carousel'),
            ('CAROUSEL_2_PLACE', 'carousel 2 place'),
            ('CHAIN', 'chain'),
            ('FIXED_2_PLACE', 'fixed 2 place'),
            ('MULTI_STOREY', 'multi storey'),
            ('STRAIGHT_LINE', 'straight line'),
        )
        return models.CharField(max_length=25, choices=PALLET_STORAGE_CONFIGURATION, **kwargs)

    @staticmethod
    def means_of_coolant_delivery(**kwargs):
        MEANS_OF_COOLANT_DELIVERY = (
            ('EXTERNAL', 'external'),
            ('THRU_SPINDLE', 'thru spindle'),
            ('THRU_TURRET', 'thru turret'),
        )
        return models.CharField(max_length=25, choices=MEANS_OF_COOLANT_DELIVERY, **kwargs)

    @staticmethod
    def interpolation(**kwargs):
        INTERPOLATION = (
            ('CIRCULAR', 'circular'),
            ('HELICAL', 'helical'),
            ('LINEAR', 'linear'),
            ('NURBS', 'nurbs'),
            ('OTHER', 'other'),
        )
        return models.CharField(max_length=25, choices=INTERPOLATION, **kwargs)

    @staticmethod
    def tool_storage_configuration(**kwargs):
        TOOL_STORAGE_CONFIGURATION = (
            ('BI_DIRECTIONAL', 'bi directional'),
            ('BOX_MATRIX', 'box matrix'),
            ('UNI_DIRECTIONAL', 'uni directional'),
        )
        return models.CharField(max_length=25, choices=TOOL_STORAGE_CONFIGURATION, **kwargs)

    @staticmethod
    def tool_compensation(**kwargs):
        TOOL_COMPENSATION = (
            ('TOOL_LENGTH', 'tool length'),
            ('TOOL_RADIUS', 'tool radius'),
        )

        return models.CharField(max_length=25, choices=TOOL_COMPENSATION, **kwargs)

    @staticmethod
    def machining_capability_profile(**kwargs):
        MACHINING_CAPABILITY_PROFILE = (
            ('BORING_CAPABILITY', 'boring capability'),
            ('DRILLING_CAPABILITY', 'drilling capability'),
            ('GUNDRILL_CAPABILITY', 'gundrill capability'),
            ('MILLING_CAPABILITY', 'milling capability'),
            ('TURNING_CAPABILITY', 'turning capability'),
        )

        return models.CharField(max_length=25, choices=MACHINING_CAPABILITY_PROFILE, **kwargs)

    @staticmethod
    def coolant_type(**kwargs):
        COOLANT_TYPE = (
            ('AIR', 'air'),
            ('FLOOD', 'flood'),
            ('MICRO', 'micro'),
            ('MIST', 'mist'),
            ('NONE', 'none'),
        )

        return models.CharField(max_length=25, choices=COOLANT_TYPE, **kwargs)

    @staticmethod
    def fixture_style(**kwargs):
        FIXTURE_STYLE = (
            ('CHUCK_FIXTURE', 'chuck fixture'),
            ('HOLE', 'hole'),
            ('T_SLOT_FIXTURE', 't slot fixture'),
            ('VACUUM', 'vacuum'),
        )

        return models.CharField(max_length=25, choices=FIXTURE_STYLE, **kwargs)

    class Meta:
        abstract = True


class Other(models.Model):
    @staticmethod
    def rot_acceleration_measure(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def rot_jerk_measure(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def jerk_measure(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    @staticmethod
    def torque_measure(**kwargs):
        return models.CharField(max_length=15, **kwargs)

    class Meta:
        abstract = True

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from machinery import schemas
from machinery.models.element_capability import ElementCapability, Chuck


class WorkTable(ElementCapability):
    rotatable = schemas.Base.boolean()
    workpiece_weight = schemas.Measure.mass(null=True, blank=True)
    fixture_style = schemas.Enumerations.fixture_style(null=True, blank=True)

    class Meta:
        abstract = True


class TSlot(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    number_of_t_slots = schemas.Measure.count()
    t_slots_size = schemas.Measure.length()
    distance_between_t_slot_centers = schemas.Measure.length()

    class Meta:
        unique_together = ('content_type', 'object_id')


class RectangularWorkTable(WorkTable):
    table_width = schemas.Measure.length()
    table_length = schemas.Measure.length()


class Pallet(WorkTable):
    random_access = schemas.Base.boolean()
    table_width = schemas.Measure.length()
    table_length = schemas.Measure.length()
    number_of_pallet = schemas.Measure.count()
    storage_configuration = schemas.Enumerations.pallet_storage_configuration(null=True, blank=True)
    pallet_change_time_minimum = schemas.Measure.time(null=True, blank=True)
    pallet_change_time_maximum = schemas.Measure.time(null=True, blank=True)
    pallet_type = schemas.Base.string(null=True, blank=True)


class CircularWorkTable(WorkTable):
    table_diameter = schemas.Measure.length()

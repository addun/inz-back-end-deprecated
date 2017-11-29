from django.db import models

from machinery import schemas
from machinery.models import MachineToolElement
from machinery.models.element_capability import ElementCapability


class TSlot(models.Model):
    number_of_t_slots = schemas.Measure.count(null=True, blank=True)
    t_slots_size = schemas.Measure.length(null=True, blank=True)
    distance_between_t_slot_centers = schemas.Measure.length(null=True, blank=True)

    class Meta:
        abstract = True


class WorkTable(ElementCapability, TSlot):
    rotatable = schemas.Base.boolean()
    workpiece_weight = schemas.Measure.mass(null=True, blank=True)
    fixture_style = schemas.Enumerations.fixture_style(null=True, blank=True)

    class Meta:
        abstract = True


class CircularWorkTable(WorkTable):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE,
                                             related_name="circularworktable")
    table_diameter = schemas.Measure.length()


class RectangularWorkTable(WorkTable):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE,
                                             related_name="rectangularworktable")
    table_width = schemas.Measure.length()
    table_length = schemas.Measure.length()


class Pallet(WorkTable):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE, related_name="pallet")
    random_access = schemas.Base.boolean()
    table_width = schemas.Measure.length()
    table_length = schemas.Measure.length()
    number_of_pallet = schemas.Measure.count()
    storage_configuration = schemas.Enumerations.pallet_storage_configuration(null=True, blank=True)
    pallet_change_time_minimum = schemas.Measure.time(null=True, blank=True)
    pallet_change_time_maximum = schemas.Measure.time(null=True, blank=True)
    pallet_type = schemas.Base.string(null=True, blank=True)

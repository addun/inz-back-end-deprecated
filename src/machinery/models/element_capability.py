from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from machinery import schemas
from machinery.models.machine_tool_element import MachineToolElement


class ElementCapability(models.Model):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE)
    description = schemas.SupportResource.text()

    class Meta:
        abstract = True


class Tailstock(ElementCapability):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE, related_name='tailstocks')
    spindle_name = schemas.SupportResource.label()
    taper = schemas.SupportResource.label()
    maximum_workpiece_weight_of_quill = schemas.Measure.mass()


class BarFeeder(ElementCapability):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE, related_name='barfeeders')
    minimum_stock_diameter = schemas.Measure.length()
    maximum_stock_diameter = schemas.Measure.length()
    maximum_stock_length = schemas.Measure.length()


class Collet(ElementCapability):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE, related_name='collets')
    collet_type = schemas.SupportResource.label()
    minimum_part_diameter = schemas.Measure.length()
    maximum_part_diameter = schemas.Measure.length()


class Chuck(ElementCapability):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    minimum_part_diameter = schemas.Measure.length()
    maximum_part_diameter = schemas.Measure.length()
    number_of_jaws = schemas.Measure.count()


class Coolant(ElementCapability):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE, related_name='coolants')
    coolant_type = schemas.Enumerations.coolant_type()
    means_of_delivery = schemas.Enumerations.means_of_coolant_delivery(null=True, blank=True)
    capacity_of_coolant_tank = schemas.Measure.volume(null=True, blank=True)
    coolant_weight = schemas.Measure.mass(null=True, blank=True)

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from machinery import schemas
from machinery.models.element_capability import ElementCapability


class ToolHandlingUnit(ElementCapability):
    class Meta:
        abstract = True


class ToolChanger(ToolHandlingUnit):
    spindle_name = schemas.SupportResource.label()
    cut_to_cut_min_tool_change_time = schemas.Measure.time(null=True, blank=True)
    cut_to_cut_max_tool_change_time = schemas.Measure.time(null=True, blank=True)


class ToolMagazine(ToolHandlingUnit):
    number_of_tools = schemas.Measure.count()
    random_access = schemas.Base.boolean()
    diameter_full = schemas.Measure.length()
    diameter_empty = schemas.Measure.length()
    tool_length = schemas.Measure.length()
    tool_weight = schemas.Measure.mass()
    storage_configuration = schemas.Enumerations.tool_compensation()


class Turret(ToolHandlingUnit):
    number_of_fixed_tools = schemas.Measure.count()
    number_of_rotating_tools = schemas.Measure.count()
    cut_to_cut_min_turret_index_time = schemas.Measure.time(null=True, blank=True)
    cut_to_cut_max_turret_index_time = schemas.Measure.time(null=True, blank=True)


class ToolAssembly(models.Model):
    tool_number = schemas.SupportResource.identifier()
    tool_type = schemas.SupportResource.label()
    tool_size = schemas.Base.string()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class SpindleName(models.Model):
    turret = models.ForeignKey(Turret, on_delete=models.CASCADE)
    spindle_name = schemas.SupportResource.label()

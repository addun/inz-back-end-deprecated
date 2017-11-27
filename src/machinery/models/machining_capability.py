from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from machinery import schemas


class MachiningCapability(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    capability = schemas.Enumerations.machining_capability_profile()
    machining_accuracy = schemas.SupportResource.text(null=True, blank=True)
    description = schemas.SupportResource.text(null=True, blank=True)

    machining_size_description = schemas.SupportResource.text(null=True, blank=True)
    machining_size_x = schemas.Measure.length()
    machining_size_y = schemas.Measure.length()
    machining_size_z = schemas.Measure.length()

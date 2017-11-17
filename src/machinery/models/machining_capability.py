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


class MachiningSize(models.Model):
    machining_capability = models.OneToOneField(MachiningCapability, primary_key=True)
    description = schemas.SupportResource.text(null=True, blank=True)
    x = schemas.Measure.length()
    y = schemas.Measure.length()
    z = schemas.Measure.length()

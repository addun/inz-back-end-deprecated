from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from machinery import schemas


class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    id = schemas.SupportResource.identifier()
    model_name = schemas.SupportResource.label()
    serial_number = schemas.SupportResource.identifier()
    manufacturer = schemas.SupportResource.label()
    date_manufactured = schemas.DateTime.calendar_date(null=True, blank=True)


class MeasuringCapability(models.Model):
    measuring_accuracy = schemas.SupportResource.text(null=True, blank=True)
    measuring_description = schemas.SupportResource.text(null=True, blank=True)

    class Meta:
        abstract = True


class MachineTool(models.Model):
    description = schemas.SupportResource.text()

    class Meta:
        abstract = True

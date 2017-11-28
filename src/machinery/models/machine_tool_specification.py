from django.db import models

from machinery import schemas
from machinery.models.others import MachineTool


class Locator(models.Model):
    business_unit = schemas.SupportResource.label(null=True, blank=True)
    plant_location = schemas.SupportResource.label(null=True, blank=True)
    building = schemas.SupportResource.label(null=True, blank=True)
    cell = schemas.SupportResource.label(null=True, blank=True)

    class Meta:
        abstract = True


class MachineToolSpecification(MachineTool, Locator):
    machine_class = schemas.Enumerations.machine_class()


class MachineKinematicAssociation(models.Model):
    kinematics = schemas.KinematicStructure.mechanism()
    machine_kinematic_association = models.OneToOneField(MachineToolSpecification)

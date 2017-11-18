from django.db import models

from machinery import schemas
from machinery.models.others import MachineTool


class MachineKinematicAssociation(models.Model):
    kinematics = schemas.KinematicStructure.mechanism()


class MachineToolSpecification(MachineTool):
    machine_kinematic_association = models.OneToOneField(MachineKinematicAssociation, primary_key=True)
    machine_class = schemas.Enumerations.machine_class()


class Locator(models.Model):
    machine_tool_specification = models.OneToOneField(MachineToolSpecification, primary_key=True)
    business_unit = schemas.SupportResource.label()
    plant_location = schemas.SupportResource.label()
    building = schemas.SupportResource.label()
    cell = schemas.SupportResource.label()

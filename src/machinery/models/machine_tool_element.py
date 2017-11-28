from django.db import models

from machinery import schemas
from machinery.models.others import MeasuringCapability
from machinery.models.machine_tool_specification import MachineToolSpecification


class MachineToolElement(MeasuringCapability):
    machine_tool_specification = models.ForeignKey(MachineToolSpecification, on_delete=models.CASCADE)
    name = schemas.SupportResource.label()
    description = schemas.SupportResource.text(null=True, blank=True)
    weight = schemas.Measure.mass(null=True, blank=True)


class ElementLinkAssociation(models.Model):
    element = models.ForeignKey(MachineToolElement)
    machine_link = schemas.KinematicStructure.kinematic_link()


class MachineElementRelationship(models.Model):
    class_name = schemas.SupportResource.label()
    latter_element = models.OneToOneField(MachineToolElement,
                                          on_delete=models.CASCADE,
                                          related_name='latter_element_to_MachineToolElement')
    former_element = models.OneToOneField(MachineToolElement,
                                          on_delete=models.CASCADE,
                                          related_name='former_element_to_MachineToolElement')

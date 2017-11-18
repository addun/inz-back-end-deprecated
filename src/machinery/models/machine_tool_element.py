from django.db import models

from machinery import schemas
from machinery.models.machine_tool_specification import MachineToolSpecification


class MachineToolElement(models.Model):
    machine_tool_specification = models.ForeignKey(MachineToolSpecification, on_delete=models.CASCADE)
    name = schemas.SupportResource.label()
    description = schemas.SupportResource.text(null=True, blank=True)
    weight = schemas.Measure.mass(null=True, blank=True)


class ElementLinkAssociation(models.Model):
    machine_tool_element = models.ForeignKey(MachineToolElement, on_delete=models.CASCADE)
    machine_link = schemas.KinematicStructure.kinematic_link()


class MachineElementRelationship(models.Model):
    class_name = schemas.SupportResource.label()
    latter_element = models.OneToOneField(MachineToolElement,
                                          on_delete=models.CASCADE,
                                          verbose_name='latter_element',
                                          related_name='latter_element_to_MachineToolElement')
    former_element = models.OneToOneField(MachineToolElement,
                                          on_delete=models.CASCADE,
                                          verbose_name='former_element',
                                          related_name='former_element_to_MachineToolElement')

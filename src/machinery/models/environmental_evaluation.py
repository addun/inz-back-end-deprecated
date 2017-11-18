from django.db import models

from machinery import schemas
from machinery.models.machine_tool_specification import MachineToolSpecification


class EnvironmentalEvaluation(models.Model):
    machine_tool_specification = models.OneToOneField(MachineToolSpecification)
    evaluation_name = schemas.SupportResource.label()
    power_in_idling = schemas.Measure.power(null=True, blank=True)
    time_for_warming_up = schemas.Measure.time(null=True, blank=True)


class StandardMachiningProcess(models.Model):
    environmental_evaluation = models.ForeignKey(EnvironmentalEvaluation, on_delete=models.CASCADE)
    process_description = schemas.SupportResource.text()
    type_of_machining = schemas.SupportResource.label()
    power = schemas.Measure.power()
    electric_power = schemas.Measure.power()


class EmissionProperty(models.Model):
    environmental_evaluation = models.ForeignKey(StandardMachiningProcess, on_delete=models.CASCADE)
    emission_type = schemas.SupportResource.label()
    weight = schemas.Measure.mass()

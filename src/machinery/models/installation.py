from django.db import models

from machinery import schemas
from machinery.models.machine_tool_specification import MachineToolSpecification


class MachineSize(models.Model):
    machine_length = schemas.Measure.length()
    machine_width = schemas.Measure.length()
    machine_height = schemas.Measure.length()

    class Meta:
        abstract = True


class Electrical(models.Model):
    electric_phase = schemas.Base.string()
    electric_power = schemas.Measure.power()
    electrical_current = schemas.Measure.electric_current()
    electrical_frequency = schemas.Base.string()
    electrical_grounding = schemas.Base.string()
    electrical_voltage = schemas.Base.real()

    class Meta:
        abstract = True


class Hydraulics(models.Model):
    type_of_hydraulic_oil = schemas.SupportResource.label(null=True, blank=True)
    pump_outlet_pressure = schemas.Measure.pressure(null=True, blank=True)
    capacity_of_hydraulics_tank = schemas.Measure.volume(null=True, blank=True)

    class Meta:
        abstract = True


class Installation(MachineSize, Electrical, Hydraulics):
    machine_tool_specification = models.OneToOneField(MachineToolSpecification, on_delete=models.CASCADE)
    weight = schemas.Measure.mass()
    air_pressure_requirement = schemas.Measure.pressure(null=True, blank=True)
    water_flow_rate = schemas.Base.real(null=True, blank=True)

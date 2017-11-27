from django.db import models

from machinery import schemas
from machinery.models.machine_tool_specification import MachineToolSpecification


class Installation(models.Model):
    machine_tool_specification = models.OneToOneField(MachineToolSpecification, on_delete=models.CASCADE)
    weight = schemas.Measure.mass()
    air_pressure_requirement = schemas.Measure.pressure(null=True, blank=True)
    water_flow_rate = schemas.Base.real(null=True, blank=True)

    # MachineSize
    machine_length = schemas.Measure.length()
    machine_width = schemas.Measure.length()
    machine_height = schemas.Measure.length()

    # Electrical
    electric_phase = schemas.Base.string()
    electric_power = schemas.Measure.power()
    electrical_current = schemas.Measure.electric_current()
    electrical_frequency = schemas.Base.string()
    electrical_grounding = schemas.Base.string()
    electrical_voltage = schemas.Base.real()

    # Hydraulics
    type_of_hydraulic_oil = schemas.SupportResource.label()
    pump_outlet_pressure = schemas.Measure.pressure()
    capacity_of_hydraulics_tank = schemas.Measure.volume()

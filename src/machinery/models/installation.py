from django.db import models

from machinery import schemas


class Installation(models.Model):
    weight = schemas.Measure.mass()
    air_pressure_requirement = schemas.Measure.pressure(null=True, blank=True)
    water_flow_rate = schemas.Base.real(null=True, blank=True)


class MachineSize(models.Model):
    installation = models.OneToOneField(Installation, on_delete=models.CASCADE, primary_key=True)
    machine_length = schemas.Measure.length()
    machine_width = schemas.Measure.length()
    machine_height = schemas.Measure.length()


class Electrical(models.Model):
    installation = models.OneToOneField(Installation, on_delete=models.CASCADE, primary_key=True)
    electric_phase = schemas.Base.string()
    electric_power = schemas.Measure.power()
    electrical_current = schemas.Measure.electric_current()
    electrical_frequency = schemas.Base.string()
    electrical_grounding = schemas.Base.string()
    electrical_voltage = schemas.Base.real()


class Hydraulics(models.Model):
    installation = models.OneToOneField(Installation, on_delete=models.CASCADE, primary_key=True)
    type_of_hydraulic_oil = schemas.SupportResource.label()
    pump_outlet_pressure = schemas.Measure.pressure()
    capacity_of_hydraulics_tank = schemas.Measure.volume()
from django.db import models

from machinery import schemas


class Installation(models.Model):
    weight = schemas.Measure.mass_measure()
    air_pressure_requirement = schemas.Measure.pressure_measure(null=True, blank=True)
    water_flow_rate = schemas.Base.real(null=True, blank=True)


class MachineSize(models.Model):
    installation = models.OneToOneField(Installation, on_delete=models.CASCADE, primary_key=True)
    machine_length = schemas.Measure.length_measure()
    machine_width = schemas.Measure.length_measure()
    machine_height = schemas.Measure.length_measure()


class Electrical(models.Model):
    electric_phase = schemas.Base.string()
    electric_power = schemas.Measure.power_measure()
    electrical_current = schemas.Measure.electric_current_measure()
    electrical_frequency = schemas.Base.string()
    electrical_grounding = schemas.Base.string()
    electrical_voltage = schemas.Base.real()


class Hydraulics(models.Model):
    installation = models.OneToOneField(Installation, on_delete=models.CASCADE, primary_key=True)
    type_of_hydraulic_oil = schemas.SupportResource.label()
    pump_outlet_pressure = schemas.Measure.pressure_measure()
    capacity_of_hydraulics_tank = schemas.Measure.volume_measur()

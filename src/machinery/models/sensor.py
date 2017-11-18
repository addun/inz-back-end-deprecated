from machinery import schemas
from machinery.models.element_capability import ElementCapability


class Sensor(ElementCapability):
    class Meta:
        abstract = True


class ToolSetting(Sensor):
    measuring_radius = schemas.Base.boolean()
    measuring_length = schemas.Base.boolean()
    measure_time = schemas.Measure.time()
    probe_type = schemas.Enumerations.probe_type()


class PartProbe(Sensor):
    probe_type = schemas.Enumerations.probe_type()
    dimensionality = schemas.Enumerations.sensor_dimensionality()
    setting_time = schemas.Measure.time()


class ToolBreakage(Sensor):
    pass

from machinery import schemas
from machinery.models.others import MachineTool


class MachineToolSpecification(MachineTool):
    machine_class = schemas.Enumerations.machine_class()

    kinematics = schemas.KinematicStructure.mechanism()

    business_unit = schemas.SupportResource.label()
    plant_location = schemas.SupportResource.label()
    building = schemas.SupportResource.label()
    cell = schemas.SupportResource.label()

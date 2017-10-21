# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . import models

# Register your models here.
admin_models = [
    models.MachineTool,
    models.MachineToolRequirements,
    models.MachiningCapability,
    models.SpindleCapability,
    models.PositioningCapability,
    models.RangeOfMotion,
    models.AxisCapability,
    models.MeasuringCapability,
    models.MachineSize
]

admin.site.register(admin_models)

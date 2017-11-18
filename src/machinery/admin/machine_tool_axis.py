# -*- coding: utf-8 -*-
from django.contrib import admin

from machinery.admin import ElementCapabilityAdmin
from machinery.models import MachineToolAxis, LinearAxis


@admin.register(MachineToolAxis)
class MachineToolAxisAdmin(ElementCapabilityAdmin):
    pass


@admin.register(LinearAxis)
class LinearAxisAdmin(MachineToolAxisAdmin):
    pass

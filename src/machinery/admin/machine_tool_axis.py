# -*- coding: utf-8 -*-
from django.contrib import admin

from machinery.models import MachineToolAxis, LinearAxis


@admin.register(MachineToolAxis)
class MachineToolAxisAdmin(admin.ModelAdmin):
    pass


@admin.register(LinearAxis)
class LinearAxisAdmin(admin.ModelAdmin):
    pass

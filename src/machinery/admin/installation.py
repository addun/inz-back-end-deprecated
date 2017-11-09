# -*- coding: utf-8 -*-
from django.contrib import admin

from machinery.models import Installation, MachineSize, Electrical, Hydraulics


# Register your models here.
class MachineSizeStackedInline(admin.StackedInline):
    model = MachineSize
    extra = 1


class ElectricalStackedInline(admin.StackedInline):
    model = Electrical
    extra = 1


class HydraulicsStackedInline(admin.StackedInline):
    model = Hydraulics
    extra = 1


@admin.register(Installation)
class InstallationAdmin(admin.ModelAdmin):
    inlines = [
        MachineSizeStackedInline,
        ElectricalStackedInline,
        HydraulicsStackedInline,
    ]

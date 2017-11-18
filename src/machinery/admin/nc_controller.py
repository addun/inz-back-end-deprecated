# -*- coding: utf-8 -*-

from django.contrib import admin

from machinery.models.nc_controller import ToolCompensationFunction, NcController, RapidTraverseOverride, \
    CuttingFeedRateOverride, CycleFunction, InterpolationFunction


# Register your models here.
class ToolCompensationFunctionStackedInline(admin.StackedInline):
    model = ToolCompensationFunction
    extra = 1


class CycleFunctionStackedInline(admin.StackedInline):
    model = CycleFunction
    extra = 1


class InterpolationFunctionStackedInline(admin.StackedInline):
    model = InterpolationFunction
    extra = 1


class CuttingFeedRateOverrideStackedInline(admin.StackedInline):
    model = CuttingFeedRateOverride
    extra = 1


class RapidTraverseOverrideStackedInline(admin.StackedInline):
    model = RapidTraverseOverride
    extra = 1


class NcControllerInline(admin.StackedInline):
    model = NcController


@admin.register(NcController)
class NcControllerAdmin(admin.ModelAdmin):
    inlines = [
        RapidTraverseOverrideStackedInline,
        CuttingFeedRateOverrideStackedInline,
        InterpolationFunctionStackedInline,
        CycleFunctionStackedInline,
        ToolCompensationFunctionStackedInline,
    ]

# -*- coding: utf-8 -*-

from django.contrib import admin

from machinery.models.nc_controller import ToolCompensationFunction, NcController, RapidTraverseOverride, \
    CuttingFeedRateOverride, CycleFunction, InterpolationFunction


class ToolCompensationFunctionInline(admin.StackedInline):
    model = ToolCompensationFunction
    extra = 1


class CycleFunctionInline(admin.StackedInline):
    model = CycleFunction
    extra = 1


class InterpolationFunctionInline(admin.StackedInline):
    model = InterpolationFunction
    min_num = 1
    extra = 0


class CuttingFeedRateOverrideInline(admin.StackedInline):
    model = CuttingFeedRateOverride
    extra = 1


class RapidTraverseOverrideInline(admin.StackedInline):
    model = RapidTraverseOverride
    extra = 1


class NcControllerInline(admin.StackedInline):
    model = NcController


@admin.register(NcController)
class NcControllerAdmin(admin.ModelAdmin):
    inlines = [
        RapidTraverseOverrideInline,
        CuttingFeedRateOverrideInline,
        InterpolationFunctionInline,
        CycleFunctionInline,
        ToolCompensationFunctionInline,
    ]

# -*- coding: utf-8 -*-

from django.contrib import admin

from machinery.models.nc_controller import ToolCompensationFunction, NcController, RapidTraverseOverride, \
    CuttingFeedRateOverride, CycleFunction, InterpolationFunction


class ToolCompensationFunctionInline(admin.StackedInline):
    model = ToolCompensationFunction
    extra = 0


class CycleFunctionInline(admin.StackedInline):
    model = CycleFunction
    extra = 0


class InterpolationFunctionInline(admin.StackedInline):
    model = InterpolationFunction
    min_num = 1
    extra = 0


class CuttingFeedRateOverrideInline(admin.StackedInline):
    model = CuttingFeedRateOverride
    extra = 0


class RapidTraverseOverrideInline(admin.StackedInline):
    model = RapidTraverseOverride
    extra = 0


class NcControllerInline(admin.StackedInline):
    model = NcController
    max_num = 1
    min_num = 1
    extra = 1


@admin.register(NcController)
class NcControllerAdmin(admin.ModelAdmin):
    inlines = [
        CycleFunctionInline,
        InterpolationFunctionInline,
        CuttingFeedRateOverrideInline,
        RapidTraverseOverrideInline,
        ToolCompensationFunctionInline,
    ]

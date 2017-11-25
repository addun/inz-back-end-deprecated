from django.contrib import admin
from django.contrib.admin.options import StackedInline

from machinery.models import EnvironmentalEvaluation, EmissionProperty, StandardMachiningProcess


class EmissionPropertyInline(admin.TabularInline):
    model = EmissionProperty
    min_num = 1


@admin.register(StandardMachiningProcess)
class StandardMachiningProcessAdmin(admin.ModelAdmin):
    inlines = [
        EmissionPropertyInline
    ]


class StandardMachiningProcessInline(admin.TabularInline):
    model = StandardMachiningProcess
    extra = 0
    show_change_link = True


@admin.register(EnvironmentalEvaluation)
class EnvironmentalEvaluationAdmin(admin.ModelAdmin):
    inlines = [
        StandardMachiningProcessInline
    ]


class EnvironmentalEvaluationInline(StackedInline):
    model = EnvironmentalEvaluation
    show_change_link = True
    extra = 0

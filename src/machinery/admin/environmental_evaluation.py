from django.contrib import admin

from machinery.models import EnvironmentalEvaluation, EmissionProperty, StandardMachiningProcess


class StandardMachiningProcessInline(admin.TabularInline):
    model = StandardMachiningProcess
    extra = 0
    show_change_link = True


class EmissionPropertyInline(admin.TabularInline):
    model = EmissionProperty
    extra = 0


@admin.register(StandardMachiningProcess)
class StandardMachiningProcessAdmin(admin.ModelAdmin):
    inlines = [
        EmissionPropertyInline
    ]


@admin.register(EnvironmentalEvaluation)
class EnvironmentalEvaluationAdmin(admin.ModelAdmin):
    inlines = [
        StandardMachiningProcessInline
    ]

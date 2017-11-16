from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from machinery.admin.element_capability import ChuckInline
from machinery.models import SpindleRange, Spindle, WorkSpindle, TaperedSpindle, StraightSpindle, ThreadedSpindle


class ToolAssemblyInline(GenericTabularInline):
    model = SpindleRange
    extra = 0


@admin.register(Spindle)
class SpindleAdmin(admin.ModelAdmin):
    inlines = [
        ToolAssemblyInline,
    ]


@admin.register(WorkSpindle)
class WorkSpindleAdmin(admin.ModelAdmin):
    inlines = [
        ToolAssemblyInline,
        ChuckInline
    ]


@admin.register(TaperedSpindle)
class TaperedSpindleAdmin(admin.ModelAdmin):
    inlines = [
        ToolAssemblyInline
    ]


@admin.register(StraightSpindle)
class StraightSpindleAdmin(admin.ModelAdmin):
    inlines = [
        ToolAssemblyInline
    ]


@admin.register(ThreadedSpindle)
class ThreadedSpindleAdmin(admin.ModelAdmin):
    inlines = [
        ToolAssemblyInline
    ]

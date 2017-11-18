from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from machinery.admin.element_capability import ChuckInline
from machinery.models import SpindleRange, Spindle, WorkSpindle, TaperedSpindle, StraightSpindle, ThreadedSpindle


class SpindleRangeInline(GenericStackedInline):
    model = SpindleRange
    extra = 0
    min_num = 1


@admin.register(Spindle)
class SpindleAdmin(admin.ModelAdmin):
    inlines = [
        SpindleRangeInline,
    ]


@admin.register(WorkSpindle)
class WorkSpindleAdmin(SpindleAdmin):
    inlines = SpindleAdmin.inlines + [
        ChuckInline,
    ]


class ToolSpindleAdmin(SpindleAdmin):
    pass


@admin.register(TaperedSpindle)
class TaperedSpindleAdmin(ToolSpindleAdmin):
    pass


@admin.register(StraightSpindle)
class StraightSpindleAdmin(ToolSpindleAdmin):
    pass


@admin.register(ThreadedSpindle)
class ThreadedSpindleAdmin(ToolSpindleAdmin):
    pass

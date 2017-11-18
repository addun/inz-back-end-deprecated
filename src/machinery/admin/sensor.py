from django.contrib import admin

from machinery.admin.others import DeviceInline
from machinery.models.sensor import ToolSetting, PartProbe, ToolBreakage


class SensorAdmin(admin.ModelAdmin):
    inlines = [
        DeviceInline
    ]


@admin.register(ToolSetting)
class ToolSettingAdmin(SensorAdmin):
    pass


@admin.register(PartProbe)
class ToolSettingAdmin(SensorAdmin):
    pass


@admin.register(ToolBreakage)
class ToolSettingAdmin(SensorAdmin):
    pass

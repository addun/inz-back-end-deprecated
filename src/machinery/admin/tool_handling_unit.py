from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from machinery.admin import ElementCapabilityAdmin
from machinery.models import ToolMagazine, ToolAssembly, Turret
from machinery.models.tool_handling_unit import ToolChanger, SpindleName


class ToolHandlingUnitAdmin(ElementCapabilityAdmin):
    pass


class ToolAssemblyInline(GenericTabularInline):
    model = ToolAssembly
    extra = 0


class SpindleNameInline(admin.TabularInline):
    model = SpindleName
    extra = 0


@admin.register(ToolChanger)
class ToolChangerAdmin(ToolHandlingUnitAdmin):
    pass


@admin.register(ToolMagazine)
class ToolMagazineAdmin(ToolHandlingUnitAdmin):
    inlines = [
        ToolAssemblyInline,
    ]


@admin.register(Turret)
class TurretAdmin(ToolHandlingUnitAdmin):
    inlines = [
        ToolAssemblyInline,
        SpindleNameInline
    ]

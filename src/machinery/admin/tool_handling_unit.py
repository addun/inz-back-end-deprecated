from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from machinery.models import ToolMagazine, ToolAssembly, Turret
from machinery.models.tool_handling_unit import ToolChanger


class ToolAssemblyInline(GenericTabularInline):
    model = ToolAssembly
    extra = 0


@admin.register(ToolMagazine)
class ToolMagazineAdmin(admin.ModelAdmin):
    inlines = [
        ToolAssemblyInline,
    ]


@admin.register(Turret)
class TurretAdmin(admin.ModelAdmin):
    inlines = [
        ToolAssemblyInline,
    ]


@admin.register(ToolChanger)
class ToolChangerAdmin(admin.ModelAdmin):
    pass

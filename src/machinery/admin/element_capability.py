from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from machinery.models import Chuck, Collet, BarFeeder, Coolant, Tailstock
from machinery.utils import experimental


class ElementCapabilityAdmin(admin.ModelAdmin):
    pass


class ChuckInline(GenericStackedInline):
    model = Chuck
    max_num = 1
    extra = 0


@admin.register(Tailstock)
class TailstockAdmin(ElementCapabilityAdmin):
    pass


@admin.register(Coolant)
class CoolantAdmin(ElementCapabilityAdmin):
    pass


@admin.register(BarFeeder)
class BarFeederAdmin(ElementCapabilityAdmin):
    pass


@admin.register(Collet)
class ColletAdmin(ElementCapabilityAdmin):
    pass


@experimental
@admin.register(Chuck)
class ChuckAdmin(ElementCapabilityAdmin):
    pass

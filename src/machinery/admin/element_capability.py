from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from machinery.models import Chuck, Collet, BarFeeder, Coolant, Tailstock


class ChuckInline(GenericStackedInline):
    model = Chuck
    max_num = 1
    extra = 0


@admin.register(Collet)
class ColletAdmin(admin.ModelAdmin):
    pass


@admin.register(BarFeeder)
class BarFeederAdmin(admin.ModelAdmin):
    pass


@admin.register(Coolant)
class CoolantAdmin(admin.ModelAdmin):
    pass


@admin.register(Tailstock)
class TailstockAdmin(admin.ModelAdmin):
    pass

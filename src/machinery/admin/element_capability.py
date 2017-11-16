from django.contrib import admin

from machinery.models import Chuck, Collet, BarFeeder, Coolant, Tailstock


@admin.register(Chuck)
class ChuckAdmin(admin.ModelAdmin):
    pass


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

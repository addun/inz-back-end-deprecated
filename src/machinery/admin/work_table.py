from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from machinery.models.work_table import RectangularWorkTable, Pallet, CircularWorkTable, TSlot


class TSlotGenericInline(GenericStackedInline):
    model = TSlot
    extra = 0
    max_num = 1


@admin.register(RectangularWorkTable)
class RectangularWorkTableAdmin(admin.ModelAdmin):
    inlines = [
        TSlotGenericInline
    ]


@admin.register(Pallet)
class PalletAdmin(admin.ModelAdmin):
    inlines = [
        TSlotGenericInline
    ]


@admin.register(CircularWorkTable)
class CircularWorkTableAdmin(admin.ModelAdmin):
    inlines = [
        TSlotGenericInline
    ]

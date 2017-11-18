from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from machinery.admin import ChuckInline, ElementCapabilityAdmin
from machinery.models import RectangularWorkTable, Pallet, CircularWorkTable, TSlot


class TSlotInline(GenericStackedInline):
    model = TSlot
    extra = 0
    max_num = 1


class WorkTable(ElementCapabilityAdmin):
    inlines = [
        TSlotInline,
        ChuckInline
    ]


@admin.register(RectangularWorkTable)
class RectangularWorkTableAdmin(WorkTable):
    pass


@admin.register(Pallet)
class PalletAdmin(WorkTable):
    pass


@admin.register(CircularWorkTable)
class CircularWorkTableAdmin(WorkTable):
    pass

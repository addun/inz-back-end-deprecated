from django.contrib import admin

from machinery.admin import ChuckInline, ElementCapabilityAdmin
from machinery.models import RectangularWorkTable, Pallet, CircularWorkTable


class WorkTable(ElementCapabilityAdmin):
    inlines = [
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

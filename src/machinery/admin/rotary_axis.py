from django.contrib import admin

from machinery.admin import MachineToolAxisAdmin
from machinery.models import ContinuousRotary, Indexing, LimitedSwing


class RotaryAxisAdmin(MachineToolAxisAdmin):
    pass


@admin.register(ContinuousRotary)
class ContinuousRotaryAdmin(RotaryAxisAdmin):
    pass


@admin.register(Indexing)
class IndexingAdmin(RotaryAxisAdmin):
    pass


@admin.register(LimitedSwing)
class LimitedSwingAdmin(RotaryAxisAdmin):
    pass

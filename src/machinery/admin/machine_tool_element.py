from django.contrib import admin

from machinery.models import MachineElementRelationship, MachineToolElement, ElementLinkAssociation, ToolChanger
from machinery.models.element_capability import Tailstock, Coolant, BarFeeder, Collet, Chuck
from machinery.models.machine_tool_axis import MachineToolAxis, LinearAxis
from machinery.models.rotary_axis import ContinuousRotary, Indexing, LimitedSwing
from machinery.models.sensor import ToolSetting, PartProbe, ToolBreakage
from machinery.models.spindle import Spindle, TaperedSpindle, StraightSpindle, ThreadedSpindle, \
    WorkSpindle
from machinery.models.tool_handling_unit import ToolMagazine, Turret
from machinery.models.work_table import RectangularWorkTable, Pallet, CircularWorkTable
from machinery.utils import experimental


def get_inline_by_model(model):
    return type(
        'DynamicInline',
        (admin.StackedInline,),
        {'model': model, 'extra': 0, 'show_change_link': True}
    )


class MachineToolElementInline(admin.TabularInline):
    model = MachineToolElement
    extra = 0
    show_change_link = True


@experimental
@admin.register(MachineToolElement)
class MachineToolElementAdmin(admin.ModelAdmin):
    inlines = [
        get_inline_by_model(ToolChanger),
        get_inline_by_model(ToolMagazine),
        get_inline_by_model(Turret),
        get_inline_by_model(MachineToolAxis),
        get_inline_by_model(LinearAxis),
        get_inline_by_model(ContinuousRotary),
        get_inline_by_model(Indexing),
        get_inline_by_model(LimitedSwing),
        get_inline_by_model(Tailstock),
        get_inline_by_model(Coolant),
        get_inline_by_model(BarFeeder),
        get_inline_by_model(Collet),
        get_inline_by_model(Spindle),
        get_inline_by_model(TaperedSpindle),
        get_inline_by_model(StraightSpindle),
        get_inline_by_model(ThreadedSpindle),
        get_inline_by_model(WorkSpindle),
        get_inline_by_model(Chuck),
        get_inline_by_model(RectangularWorkTable),
        get_inline_by_model(Pallet),
        get_inline_by_model(CircularWorkTable),
        get_inline_by_model(ToolSetting),
        get_inline_by_model(PartProbe),
        get_inline_by_model(ToolBreakage),
    ]


@admin.register(MachineElementRelationship)
class MachineElementRelationshipAdmin(admin.ModelAdmin):
    pass


@admin.register(ElementLinkAssociation)
class ElementLinkAssociationAdmin(admin.ModelAdmin):
    pass

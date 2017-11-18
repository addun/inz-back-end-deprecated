from django.contrib import admin

from machinery.models import MachineElementRelationship, MachineToolElement, ElementLinkAssociation


class MachineToolElementInline(admin.TabularInline):
    model = MachineToolElement
    extra = 0
    show_change_link = True


@admin.register(MachineElementRelationship)
class MachineElementRelationshipAdmin(admin.ModelAdmin):
    pass


@admin.register(ElementLinkAssociation)
class ElementLinkAssociationAdmin(admin.ModelAdmin):
    pass


@admin.register(MachineToolElement)
class MachineToolElementAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin

from machinery.models import MachineElementRelationship, MachineToolElement, ElementLinkAssociation


@admin.register(MachineElementRelationship)
class MachineElementRelationshipAdmin(admin.ModelAdmin):
    pass


@admin.register(ElementLinkAssociation)
class ElementLinkAssociationAdmin(admin.ModelAdmin):
    pass


@admin.register(MachineToolElement)
class MachineToolElementAdmin(admin.ModelAdmin):
    pass

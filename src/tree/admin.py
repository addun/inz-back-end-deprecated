# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from tree.models import Node, MachineToolSpecificationInNode


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = [
        'value',
        'parent'
    ]


@admin.register(MachineToolSpecificationInNode)
class MachineToolSpecificationInNodeAdmin(admin.ModelAdmin):
    pass

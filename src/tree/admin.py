# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from tree.models import Node


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'parent'
    ]

# -*- coding: utf-8 -*-
from django.contrib import admin

from machinery.models import Installation


@admin.register(Installation)
class InstallationAdmin(admin.ModelAdmin):
    pass


class InstallationInline(admin.StackedInline):
    model = Installation
    show_change_link = True

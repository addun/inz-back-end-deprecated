# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from enginery.models import MachineToolSpecification


@admin.register(MachineToolSpecification)
class MachineToolSpecificationAdmin(admin.ModelAdmin):
    pass

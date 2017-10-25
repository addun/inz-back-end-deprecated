# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse

from . import models

# Register your models here.
admin_models = [
    models.MachineTool,
    models.MachiningCapability,
    models.SpindleCapability,
    models.PositioningCapability,
    models.RangeOfMotion,
    models.AxisCapability,
    models.MeasuringCapability,
    models.MachineSize
]


@admin.register(models.MachineToolRequirements)
class MachineToolRequirementsAdmin(admin.ModelAdmin):
    list_display = ['description', 'get_xml']

    def get_xml(self, obj):
        link = "%s?format=xml" % reverse('machine-tool-requirements-detail', args=[obj.id])
        return '<a href="{0}">Get XML</a>'.format(link)

    get_xml.allow_tags = True


admin.site.register(admin_models)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *


class ExtendInline(admin.TabularInline):
    model = Extend
    extra = 0


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = ('image_preview',)


class MachineAdmin(admin.ModelAdmin):
    inlines = (ExtendInline, ImageInline,)


admin.site.register(Machine, MachineAdmin)

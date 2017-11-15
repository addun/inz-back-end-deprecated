from django.contrib import admin

from machinery.models import ContinuousRotary, Indexing, LimitedSwing


@admin.register(ContinuousRotary)
class ContinuousRotaryAdmin(admin.ModelAdmin):
    pass


@admin.register(Indexing)
class IndexingAdmin(admin.ModelAdmin):
    pass


@admin.register(LimitedSwing)
class LimitedSwingAdmin(admin.ModelAdmin):
    pass

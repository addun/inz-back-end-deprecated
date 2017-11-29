from camel_snake_kebab import *
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework import viewsets

from machinery.models import ToolSetting, PartProbe, ToolBreakage
from machinery.serializers.utils import get_serializer
from machinery.views.machine_tool_element import MachineToolElementViewSet


class CustomRouter(routers.DefaultRouter):
    def register_by_model(self, model):
        router_name = kebab_case(model.__name__)
        self.register(r'%s' % router_name, self.get_view_set(model))

    def get_view_set(self, model):
        return type(
            'DynamicViewSet', (viewsets.ModelViewSet,),
            {
                'queryset': model.objects.all(),
                'serializer_class': get_serializer(model),
            }
        )


router = CustomRouter()
router.register_by_model(ToolSetting)
router.register_by_model(PartProbe)
router.register_by_model(ToolBreakage)
router.register('machine-tool-element', MachineToolElementViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]

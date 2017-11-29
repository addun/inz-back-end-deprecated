from camel_snake_kebab import *
from django.conf.urls import url, include
from rest_framework import routers, serializers
from rest_framework import viewsets

from machinery.models import ToolSetting, PartProbe, ToolBreakage


class CustomRouter(routers.DefaultRouter):

    def register_by_model(self, model):
        router_name = kebab_case(model.__name__)
        self.register(r'%s' % router_name, self.get_view_set(model))

    def get_view_set(self, model):
        return type(
            'DynamicViewSet', (viewsets.ModelViewSet,),
            {
                'queryset': model.objects.all(),
                'serializer_class': self.get_serializer(model),
            }
        )

    def get_serializer(self, model):
        meta = type('Meta', (object,), {
            'model': model,
            'fields': '__all__'
        })

        dynamic_serializer = type(
            'DynamicSerializer', (serializers.ModelSerializer,), {
                'Meta': meta
            }
        )
        return dynamic_serializer


router = CustomRouter()
router.register_by_model(ToolSetting)
router.register_by_model(PartProbe)
router.register_by_model(ToolBreakage)

urlpatterns = [
    url(r'^', include(router.urls))
]

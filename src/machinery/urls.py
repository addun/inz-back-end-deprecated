from django.conf.urls import url, include
from rest_framework import routers, serializers
from rest_framework import viewsets

from machinery.models import ToolSetting
from machinery.views import MachineToolAxisViewSet, LinearAxisViewSet, ContinuousRotaryViewSet, IndexingViewSet, \
    LimitedSwingViewSet


def get_view_set(model):
    return type(
        'DynamicViewSet', (viewsets.ModelViewSet,),
        {
            'queryset': model.objects.all(),
            'serializer_class': get_serializer(model),
        }
    )


def get_serializer(model):
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


router = routers.DefaultRouter()
router.register(r'machine-tool-axis', MachineToolAxisViewSet)
router.register(r'linear-axis', LinearAxisViewSet)

router.register(r'continuous-rotary', ContinuousRotaryViewSet)
router.register(r'indexing', IndexingViewSet)
router.register(r'limited-swing', LimitedSwingViewSet)

router.register(r'tool-setting', get_view_set(ToolSetting))

urlpatterns = [
    url(r'^', include(router.urls))
]

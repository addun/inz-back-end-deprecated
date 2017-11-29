from django.conf.urls import url, include
from rest_framework import routers

from machinery.views import MachineToolAxisViewSet, LinearAxisViewSet, ContinuousRotaryViewSet, IndexingViewSet, \
    LimitedSwingViewSet

router = routers.DefaultRouter()
router.register(r'machine-tool-axis', MachineToolAxisViewSet)
router.register(r'linear-axis', LinearAxisViewSet)

router.register(r'continuous-rotary', ContinuousRotaryViewSet)
router.register(r'indexing', IndexingViewSet)
router.register(r'limited-swing', LimitedSwingViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]

from django.conf.urls import url, include
from rest_framework import routers

from machinery.views import MachineToolAxisViewSet, LinearAxisViewSet

router = routers.DefaultRouter()
router.register(r'machine-tool-axis', MachineToolAxisViewSet)
router.register(r'linear-axis', LinearAxisViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]

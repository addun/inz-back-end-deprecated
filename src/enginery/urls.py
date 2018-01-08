from django.conf.urls import url, include
from rest_framework import routers

from enginery.views import MachineToolSpecificationSet

router = routers.DefaultRouter()
router.register('asdfawef', MachineToolSpecificationSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

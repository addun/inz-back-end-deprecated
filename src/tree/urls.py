from django.conf.urls import url, include
from rest_framework import routers

from tree.views import NodeViewSet, NodeTreeList

router = routers.DefaultRouter()
router.register('nodes', NodeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^structure/$', NodeTreeList.as_view(), name='tree_structure'),
]

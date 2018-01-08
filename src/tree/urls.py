from django.conf.urls import url, include
from rest_framework import routers

from tree.views import NodeViewSet, NodeTreeList, MachineToolSpecificationInNodeViewSet, \
    MachineToolSpecificationInNodeList

router = routers.DefaultRouter()
router.register('nodes', NodeViewSet)
router.register('machine-tool-specification-in-node', MachineToolSpecificationInNodeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^structure/$', NodeTreeList.as_view(), name='node_structure'),
    url(r'^tesetset/(?P<pk>\d+)/$', MachineToolSpecificationInNodeList.as_view(), name='node_structure22'),
]

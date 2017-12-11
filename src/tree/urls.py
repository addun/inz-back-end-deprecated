from django.conf.urls import url, include
from rest_framework import routers

from tree.views import NodeViewSet, NodeTreeList, MachineToolRequirementInNode, NodeMachineToolRequirementViewSet

router = routers.DefaultRouter()
router.register('nodes', NodeViewSet)
router.register('node-machine-tool-requirement', NodeMachineToolRequirementViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^structure/$', NodeTreeList.as_view(), name='node_structure'),
    url(r'^machine-tool-requirement-in-node/(?P<pk>[0-9]+)/$', MachineToolRequirementInNode.as_view(),
        name='machine_tool_requirement_with_tag'),
]

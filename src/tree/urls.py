from django.conf.urls import url, include
from rest_framework import routers

from tree.views import NodeViewSet, NodeTreeList, TagViewSet, TagMachineToolRequirementViewSet, \
    MachineToolRequirementWithTag

router = routers.DefaultRouter()
router.register('nodes', NodeViewSet)
router.register('tags', TagViewSet)
router.register('tags-machine-tool-requirements', TagMachineToolRequirementViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^structure/$', NodeTreeList.as_view(), name='tree_structure'),
    url(r'^machine-tool-requirement-with-tag/(?P<pk>[0-9]+)/$', MachineToolRequirementWithTag.as_view(),
        name='machine_tool_requirement_with_tag'),
]

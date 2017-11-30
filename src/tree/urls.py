from django.conf.urls import url, include
from rest_framework import routers

from tree.views import NodeViewSet, NodeChildrenList

router = routers.DefaultRouter()
router.register('nodes', NodeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^nodes/(?P<pk>[0-9]+)/children/$', NodeChildrenList.as_view(), name='node_children'),
]

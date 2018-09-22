# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from rest_framework import viewsets, generics

from tree.models import Node, MachineToolSpecificationInNode
from tree.serializers import NodeSerializer, NodeTreeSerializer, MachineToolSpecificationInNodeSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class NodeTreeList(generics.ListAPIView):
    serializer_class = NodeTreeSerializer
    queryset = Node.objects.filter(parent__isnull=True)



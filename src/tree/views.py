# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from rest_framework import viewsets, generics

from enginery.models import MachineToolSpecification
from enginery.serializers import MachineToolSpecificationSerializer
from tree.models import Node, MachineToolSpecificationInNode
from tree.serializers import NodeSerializer, NodeTreeSerializer, MachineToolSpecificationInNodeSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class NodeTreeList(generics.ListAPIView):
    serializer_class = NodeTreeSerializer
    queryset = Node.objects.filter(parent__isnull=True)


class MachineToolSpecificationInNodeViewSet(viewsets.ModelViewSet):
    serializer_class = MachineToolSpecificationInNodeSerializer
    queryset = MachineToolSpecificationInNode.objects.all()


class MachineToolSpecificationInNodeList(generics.ListAPIView):
    serializer_class = MachineToolSpecificationSerializer

    def get_queryset(self):
        node_pk = self.kwargs['pk']
        return MachineToolSpecification.objects.filter(machinetoolspecificationinnode__node=node_pk)

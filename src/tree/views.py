# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

# Create your views here.
from rest_framework import viewsets, generics

from machinery.models import MachineToolRequirement
from machinery.serializers.machine_tool_requirement import MachineToolRequirementSerializer
from tree.models import Node, NodeMachineToolRequirement
from tree.serializers import NodeSerializer, NodeTreeSerializer, NodeMachineToolRequirementSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class NodeMachineToolRequirementViewSet(viewsets.ModelViewSet):
    queryset = NodeMachineToolRequirement.objects.all()
    serializer_class = NodeMachineToolRequirementSerializer


class NodeTreeList(generics.ListAPIView):
    serializer_class = NodeTreeSerializer
    queryset = Node.objects.filter(parent__isnull=True)


class MachineToolRequirementInNode(generics.ListAPIView):
    serializer_class = MachineToolRequirementSerializer

    def get_queryset(self):
        node_pk = self.kwargs['pk']
        return MachineToolRequirement.objects.filter(nodemachinetoolrequirement__node=node_pk)

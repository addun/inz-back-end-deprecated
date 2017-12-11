# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

# Create your views here.
from rest_framework import viewsets, generics

from machinery.models import MachineToolRequirement
from machinery.serializers.machine_tool_requirement import MachineToolRequirementSerializer
from tree.models import Node, Tag, TagMachineToolRequirement
from tree.serializers import NodeSerializer, NodeTreeSerializer, TagSerializer, TagMachineToolRequirementSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class TagMachineToolRequirementViewSet(viewsets.ModelViewSet):
    queryset = TagMachineToolRequirement.objects.all()
    serializer_class = TagMachineToolRequirementSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class NodeTreeList(generics.ListAPIView):
    serializer_class = NodeTreeSerializer
    queryset = Node.objects.filter(parent__isnull=True)


class MachineToolRequirementWithTag(generics.ListAPIView):
    serializer_class = MachineToolRequirementSerializer

    def get_queryset(self):
        tag_pk = self.kwargs['pk']
        return MachineToolRequirement.objects.filter(tagmachinetoolrequirement__tag=tag_pk)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from rest_framework import viewsets, generics

from tree.models import Node
from tree.serializers import NodeSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class NodeChildrenList(generics.ListAPIView):
    serializer_class = NodeSerializer

    def get_queryset(self):
        parent = self.kwargs['pk']
        if int(parent) == 0:
            return Node.objects.filter(parent__isnull=True)
        else:
            return Node.objects.filter(parent=parent)


class NodeHierarchyList(generics.ListAPIView):
    serializer_class = NodeSerializer

    def get_queryset(self):
        return Node.objects.filter(parent__isnull=True)

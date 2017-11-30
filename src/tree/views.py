# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from rest_framework import viewsets

from tree.models import Node
from tree.serializers import NodeSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

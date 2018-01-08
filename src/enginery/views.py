# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

# Create your views here.
from enginery.models import MachineToolSpecification
from enginery.serializers import MachineToolSpecificationSerializer


class MachineToolSpecificationSet(viewsets.ModelViewSet):
    queryset = MachineToolSpecification.objects.all()
    serializer_class = MachineToolSpecificationSerializer

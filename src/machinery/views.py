# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

# Create your views here.
from .models import MachineToolRequirements
from .serializers import MachineToolRequirementsSerializer


class MachineToolRequirementsList(generics.ListAPIView):
    queryset = MachineToolRequirements.objects.all()
    serializer_class = MachineToolRequirementsSerializer

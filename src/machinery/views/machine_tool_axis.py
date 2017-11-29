from rest_framework import viewsets

from machinery.models import MachineToolAxis, LinearAxis
from machinery.serializers import MachineToolAxisSerializer, LinearAxisSerializer


class MachineToolAxisViewSet(viewsets.ModelViewSet):
    queryset = MachineToolAxis.objects.all()
    serializer_class = MachineToolAxisSerializer


class LinearAxisViewSet(viewsets.ModelViewSet):
    queryset = LinearAxis.objects.all()
    serializer_class = LinearAxisSerializer

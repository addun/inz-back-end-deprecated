from rest_framework import viewsets

from machinery.models import MachineToolElement
from machinery.serializers.machine_tool_element import MachineToolElementSerializer


class MachineToolElementViewSet(viewsets.ModelViewSet):
    queryset = MachineToolElement.objects.all()
    serializer_class = MachineToolElementSerializer

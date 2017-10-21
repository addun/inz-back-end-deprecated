from rest_framework import serializers

from .models import *


class MachineToolRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineToolRequirements
        fields = "__all__"
        depth = 10

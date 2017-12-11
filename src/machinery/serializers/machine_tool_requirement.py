from rest_framework import serializers

from machinery.models import MachineToolRequirement


class MachineToolRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineToolRequirement
        fields = '__all__'

from rest_framework import serializers

from machinery.models.machine_tool_axis import MachineToolAxis, LinearAxis


class MachineToolAxisSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineToolAxis
        fields = '__all__'


class LinearAxisSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinearAxis
        fields = '__all__'

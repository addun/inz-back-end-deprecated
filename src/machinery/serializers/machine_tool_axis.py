from rest_framework import serializers

from machinery.models.machine_tool_axis import MachineToolAxis, LinearAxis


class MachineToolAxisSerializers(serializers.ModelSerializer):
    class Meta:
        model = MachineToolAxis
        fields = '__all__'


class LinearAxisSerializers(serializers.ModelSerializer):
    class Meta:
        model = LinearAxis
        fields = '__all__'

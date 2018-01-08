from rest_framework import serializers

from enginery.models import MachineToolSpecification


class MachineToolSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineToolSpecification
        fields = '__all__'

from rest_framework import serializers

from tree.models import Node, MachineToolSpecificationInNode


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class NodeTreeSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Node
        fields = '__all__'


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'


class MachineToolSpecificationInNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineToolSpecificationInNode
        fields = '__all__'

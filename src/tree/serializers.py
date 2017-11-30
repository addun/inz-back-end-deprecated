from rest_framework import serializers

from tree.models import Node


class NodeSerializer(serializers.ModelSerializer):
    hasChildren = serializers.SerializerMethodField()

    class Meta:
        model = Node
        fields = [
            'parent',
            'name',
            'id',
            'hasChildren'
        ]

    def get_hasChildren(self, obj):
        children = Node.objects.filter(parent=obj.id)
        if children:
            return True
        else:
            return False

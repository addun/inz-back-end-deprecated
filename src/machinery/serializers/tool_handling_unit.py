from rest_framework import serializers

from machinery.models.tool_handling_unit import ToolChanger, ToolMagazine, Turret, SpindleName, ToolAssembly


class ToolChangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolChanger
        fields = '__all__'


class ToolMagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolMagazine
        fields = '__all__'


class TurretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turret
        fields = '__all__'

# ToDo Create ToolAssembly serializer for GFK


class SpindleNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpindleName
        fields = '__all__'


class ToolAssemblySerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolAssembly
        fields = '__all__'

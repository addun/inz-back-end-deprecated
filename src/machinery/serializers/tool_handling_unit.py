from rest_framework import serializers

from machinery.models.tool_handling_unit import ToolChanger, ToolMagazine, Turret, SpindleName, ToolAssembly


class ToolChangerSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToolChanger
        fields = '__all__'


class ToolMagazineSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToolMagazine
        fields = '__all__'


class TurretSerializers(serializers.ModelSerializer):
    class Meta:
        model = Turret
        fields = '__all__'


class SpindleNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpindleName
        fields = '__all__'


class ToolAssemblySerializers(serializers.ModelSerializer):
    class Meta:
        model = ToolAssembly
        fields = '__all__'

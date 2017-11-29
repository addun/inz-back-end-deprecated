from rest_framework import serializers

from machinery.models import ToolSetting, PartProbe, ToolBreakage


class ToolSettingSerializer(serializers.ModelSerializer):
    class Meta:
        models = ToolSetting
        fields = '__all__'


class PartProbeSerializer(serializers.ModelSerializer):
    class Meta:
        models = PartProbe
        fields = '__all__'


class ToolBreakageSerializer(serializers.ModelSerializer):
    class Meta:
        models = ToolBreakage
        fields = '__all__'

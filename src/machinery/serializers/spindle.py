from rest_framework import serializers

from machinery.models import Spindle, ThreadedSpindle, StraightSpindle, WorkSpindle, TaperedSpindle, ToolSpindle


class SpindleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spindle
        fields = '__all__'


# ToDo Create SpindleRange serializer for GFK


class ToolSpindleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolSpindle
        fields = '__all__'


class TaperedSpindleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaperedSpindle
        fields = '__all__'


class StraightSpindleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StraightSpindle
        fields = '__all__'


class ThreadedSpindleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadedSpindle
        fields = '__all__'


class WorkSpindleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpindle
        fields = '__all__'

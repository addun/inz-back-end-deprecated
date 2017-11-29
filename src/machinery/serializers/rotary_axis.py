from rest_framework import serializers

from machinery.models import RotaryAxis, ContinuousRotary, LimitedSwing, Indexing


class RotaryAxisSerializers(serializers.ModelSerializer):
    class Meta:
        model = RotaryAxis
        fields = '__all__'


class ContinuousRotarySerializers(serializers.ModelSerializer):
    class Meta:
        model = ContinuousRotary
        fields = '__all__'


class IndexingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Indexing
        fields = '__all__'


class LimitedSwingSerializers(serializers.ModelSerializer):
    class Meta:
        model = LimitedSwing
        fields = '__all__'

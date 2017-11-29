from rest_framework import serializers

from machinery.models import ContinuousRotary, LimitedSwing, Indexing


class ContinuousRotarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContinuousRotary
        fields = '__all__'


class IndexingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indexing
        fields = '__all__'


class LimitedSwingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LimitedSwing
        fields = '__all__'

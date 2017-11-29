from rest_framework import serializers

from machinery.models import CircularWorkTable, RectangularWorkTable, Pallet


class CircularWorkTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircularWorkTable
        fields = '__all__'


class RectangularWorkTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RectangularWorkTable
        fields = '__all__'


class PalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pallet
        fields = '__all__'

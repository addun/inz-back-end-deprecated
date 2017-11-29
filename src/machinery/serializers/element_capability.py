from rest_framework import serializers

from machinery.models import Tailstock, BarFeeder, Collet, Chuck, Coolant


class TailstockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tailstock
        fields = '__all__'


class BarFeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarFeeder
        fields = '__all__'


class ColletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collet
        fields = '__all__'


class ChuckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chuck
        fields = '__all__'


class CoolantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coolant
        fields = '__all__'

# ToDo: Chuck Generic FK

from rest_framework import serializers
from .models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    passengers = serializers.IntegerField(required=True)
    class Meta:
        model = Airplane
        fields = ['id', 'passengers']

from rest_framework import serializers
from .models import Turista

class TuristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turista
        fields = ['id', 'email', 'nombre']

class RegistroTuristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turista
        fields = ['email', 'nombre', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return Turista.objects.create_user(**validated_data)

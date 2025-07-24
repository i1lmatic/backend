from rest_framework import serializers
from .models import Empresa
from django.contrib.auth.hashers import make_password

class EmpresaSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Empresa
        fields = ['id', 'nombre', 'email', 'password', 'ruc', 'telefono', 'direccion']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
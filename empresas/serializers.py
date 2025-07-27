from rest_framework import serializers
from .models import Empresa
from django.contrib.auth import authenticate

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id', 'email', 'nombre_comercial', 'direccion', 'telefono']

class EmpresaRegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Empresa
        fields = ['email', 'nombre_comercial', 'password']

    def create(self, validated_data):
        return Empresa.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Credenciales inválidas')
        data['user'] = user
        return data

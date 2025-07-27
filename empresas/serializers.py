from rest_framework import serializers
from .models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Empresa
        exclude = ['user_permissions', 'groups']  # Ocultamos campos internos

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        empresa = Empresa(**validated_data)
        if password:
            empresa.set_password(password)
        else:
            empresa.set_password(Empresa.objects.make_random_password())
        empresa.save()
        return empresa

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
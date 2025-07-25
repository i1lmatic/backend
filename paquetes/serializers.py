from rest_framework import serializers
from paquetes.models import Paquete

class PaqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paquete
        fields = ['nombre', 'descripcion', 'precio', 'fecha_inicio', 'fecha_fin', 'disponible']  # Excluimos 'empresa'

    def create(self, validated_data):
        # Asigna automáticamente la empresa logueada (sin pedirla en el request)
        empresa = self.context['request'].user  # ¡El usuario ES la empresa!
        return Paquete.objects.create(empresa=empresa, **validated_data)
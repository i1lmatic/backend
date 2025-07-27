from rest_framework import generics, status, serializers
from rest_framework.response import Response
from .models import Empresa
from .serializers import EmpresaSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Serializer personalizado para incluir campos extra y verificar empresa
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Solo permitir login si la empresa está verificada
        if not self.user.verificado:
            raise serializers.ValidationError('Esta empresa no ha sido verificada')
        data['empresa_id'] = self.user.id
        data['nombre'] = self.user.nombre
        data['email'] = self.user.email
        return data

class EmpresaLogin(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class EmpresaList(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
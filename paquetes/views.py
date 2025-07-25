from rest_framework import viewsets, permissions
from paquetes.models import Paquete
from paquetes.serializers import PaqueteSerializer

class PaqueteViewSet(viewsets.ModelViewSet):
    serializer_class = PaqueteSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo empresas logueadas

    def get_queryset(self):
        # Filtra paquetes solo de la empresa logueada
        return Paquete.objects.filter(empresa=self.request.user)

    def perform_create(self, serializer):
        # Asigna automáticamente la empresa al crear
        serializer.save(empresa=self.request.user)
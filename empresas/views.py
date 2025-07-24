from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Empresa
from .serializers import EmpresaSerializer

class EmpresaCreateView(generics.CreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.AllowAny]  # Cambiar a IsAdminUser en producción

class EmpresaDetailView(generics.RetrieveUpdateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]
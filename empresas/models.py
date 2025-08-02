# models.py
from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='empresa')
    nombre_comercial = models.CharField(max_length=255)
    direccion = models.TextField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nombre_comercial

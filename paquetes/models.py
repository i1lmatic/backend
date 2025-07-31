# paquetes/models.py
from django.db import models
from empresas.models import Empresa

class PaqueteTuristico(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='paquetes')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cupos_disponibles = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.titulo} - {self.empresa.nombre_comercial}"

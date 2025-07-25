from django.db import models
from empresas.models import Empresa  # Importa tu modelo Empresa personalizado

class Paquete(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    disponible = models.BooleanField(default=True)
    empresa = models.ForeignKey(
        Empresa, 
        on_delete=models.CASCADE,
        editable=False  # Evita que se modifique manualmente
    )

    def __str__(self):
        return f"{self.nombre} (Empresa: {self.empresa.nombre})"
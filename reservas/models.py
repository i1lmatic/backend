# reservas/models.py
from django.db import models
from turistas.models import Turista
from paquetes.models import PaqueteTuristico

class Reserva(models.Model):
    turista = models.ForeignKey(Turista, on_delete=models.CASCADE, related_name='reservas')
    paquete = models.ForeignKey(PaqueteTuristico, on_delete=models.CASCADE, related_name='reservas')
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    cantidad_personas = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada')
    ], default='pendiente')

    def __str__(self):
        return f"Reserva de {self.turista.email} para {self.paquete.titulo}"

from django.db import models
from django.contrib.auth.models import AbstractUser

class Empresa(AbstractUser):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    ruc = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    verificado = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)

    # Personalizamos los nombres de los campos de acceso inverso para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='empresa_set',
        related_query_name='empresa'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='empresa_set',
        related_query_name='empresa'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def save(self, *args, **kwargs):
        # Si la contraseña está en texto plano, la hasheamos
        if self.pk is None or not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
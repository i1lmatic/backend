from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

class EmpresaManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        empresa = self.model(email=self.normalize_email(email), **extra_fields)
        empresa.set_password(password)
        empresa.save(using=self._db)
        return empresa

class Empresa(AbstractBaseUser):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    ruc = models.CharField(
        max_length=20,
        unique=True,
        validators=[RegexValidator(regex='^[0-9]{11}$', message='RUC debe tener 11 dígitos')]
    )
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'ruc']

    objects = EmpresaManager()

    def __str__(self):
        return self.nombre
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group,Permission

class EmpresaManager(BaseUserManager):
    def create_user(self, email, nombre_comercial, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        empresa = self.model(email=email, nombre_comercial=nombre_comercial, **extra_fields)
        empresa.set_password(password)
        empresa.save(using=self._db)
        return empresa

    def create_superuser(self, email, nombre_comercial, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, nombre_comercial, password, **extra_fields)

class Empresa(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre_comercial = models.CharField(max_length=255)
    direccion = models.TextField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    
    objects = EmpresaManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre_comercial']
    groups = models.ManyToManyField(
        Group,
        related_name='empresa_set',  # 👈 nombre único
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='empresa_permissions',
        blank=True
    )

    def __str__(self):
        return self.nombre_comercial

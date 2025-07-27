from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group,Permission

class TuristaManager(BaseUserManager):
    def create_user(self, email, nombre, password=None, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        email = self.normalize_email(email)
        turista = self.model(email=email, nombre=nombre, **extra_fields)
        turista.set_password(password)
        turista.save(using=self._db)
        return turista

    def create_superuser(self, email, nombre, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, nombre, password, **extra_fields)

class Turista(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = TuristaManager()


    groups = models.ManyToManyField(
        Group,
        related_name='turista_set',  # 👈 nombre único
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='turista_permissions',
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.email

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Empresa

class EmpresaAdmin(UserAdmin):
    model = Empresa
    list_display = ('nombre', 'email', 'ruc', 'verificado', 'is_active', 'is_staff')
    search_fields = ('nombre', 'email', 'ruc')
    list_filter = ('verificado', 'is_active', 'is_staff')
    ordering = ('nombre',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('nombre', 'ruc', 'telefono', 'direccion', 'verificado', 'creado_en')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre', 'ruc', 'telefono', 'direccion', 'verificado', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

admin.site.register(Empresa, EmpresaAdmin)
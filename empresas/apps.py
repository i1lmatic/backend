from django.apps import AppConfig

class EmpresasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'empresas'
    label = 'empresas'  # Esto es importante para evitar conflictos de nombres
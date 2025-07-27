from django.urls import path
from .views import RegistroEmpresaView, LoginEmpresaView, PerfilEmpresaView

urlpatterns = [
    path('registro/', RegistroEmpresaView.as_view(), name='registro_empresa'),
    path('login/', LoginEmpresaView.as_view(), name='login_empresa'),
    path('perfil/', PerfilEmpresaView.as_view(), name='perfil_empresa'),
]

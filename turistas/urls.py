from django.urls import path
from .views import RegistroTuristaView, LoginTuristaView, PerfilTuristaView

urlpatterns = [
    path('registro/', RegistroTuristaView.as_view()),
    path('login/', LoginTuristaView.as_view()),
    path('perfil/', PerfilTuristaView.as_view()),
]

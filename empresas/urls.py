from django.urls import path
from .views import EmpresaCreateView, EmpresaDetailView, EmpresaLoginView

urlpatterns = [
    path('registro/', EmpresaCreateView.as_view(), name='empresa-registro'),
    path('<int:pk>/', EmpresaDetailView.as_view(), name='empresa-detalle'),
    path('login/', EmpresaLoginView.as_view(), name='empresa-login'),  # ¡Nueva ruta!
]
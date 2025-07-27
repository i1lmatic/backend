from django.urls import path
from .views import EmpresaList, EmpresaDetail, EmpresaLogin

urlpatterns = [
    path('api/empresas/', EmpresaList.as_view(), name='empresa-list'),
    path('api/empresas/<int:pk>/', EmpresaDetail.as_view(), name='empresa-detail'),
    path('api/login/', EmpresaLogin.as_view(), name='login-empresa'),
]
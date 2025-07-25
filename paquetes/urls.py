from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaqueteViewSet

router = DefaultRouter()
router.register(r'', PaqueteViewSet, basename='paquete')  # 👈 Ruta base vacía

urlpatterns = [
    path('', include(router.urls)),
]
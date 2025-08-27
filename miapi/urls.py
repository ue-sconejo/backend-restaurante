from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientesViewSet, EmpleadosViewSet, MesasViewSet

router = DefaultRouter()
router.register(r'clientes', ClientesViewSet)
router.register(r'empleados', EmpleadosViewSet)
router.register(r'mesas', MesasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
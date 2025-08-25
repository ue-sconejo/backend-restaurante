from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('miapi.urls')),  # Reemplaza 'tu_app' por el nombre real
]
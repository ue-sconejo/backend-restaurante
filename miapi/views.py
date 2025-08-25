from django.shortcuts import render

from rest_framework import viewsets
from .models import Empleados 
from .serializers import EmpleadosSerializer

class EmpleadoViewSet(viewsets.ModelViewSet): 
    queryset = Empleados.objects.all() 
    serializer_class = EmpleadosSerializer 

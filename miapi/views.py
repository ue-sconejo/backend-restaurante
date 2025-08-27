from rest_framework import viewsets
from .models import Clientes, Empleados, EstadoReserva, Mesas, Reservas
from .serializers import ClientesSerializer, EmpleadosSerializer, MesasSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer

class MesasViewSet(viewsets.ModelViewSet):
    queryset = Mesas.objects.all()
    serializer_class = MesasSerializer
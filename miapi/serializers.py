from rest_framework import serializers
from .models import Clientes, Empleados, EstadoReserva, Mesas, Reservas

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'
        
class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'
        
class MesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesas
        fields = '__all__'

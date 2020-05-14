from rest_framework import serializers

from tecninfor_recibos.models import Empleados

class EmpleadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empleados
        fields = '__all__'


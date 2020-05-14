from rest_framework import serializers

from tecninfor_recibos.models import Fechas


class FechaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fechas
        fields = '__all__'

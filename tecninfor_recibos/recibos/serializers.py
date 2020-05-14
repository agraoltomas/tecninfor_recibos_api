from rest_framework import serializers
from tecninfor_recibos.models import Recibos


class ReciboDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recibos
        fields = ['id','cuil','periodo','tipo']

class ReciboBytesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recibos
        fields = ['id','cuil','bytes']

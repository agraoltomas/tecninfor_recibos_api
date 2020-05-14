from rest_framework import serializers

from tecninfor_recibos.models import Login


class LoginSerializer(serializers.ModelSerializer):

    class Meta:

        model = Login
        exclude = ['password','salt']

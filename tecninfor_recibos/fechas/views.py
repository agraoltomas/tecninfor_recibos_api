from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from tecninfor_recibos.models import Fechas
from fechas.serializers import FechaSerializer

# Create your views here.


class FechasList(APIView):
    serializer_class = FechaSerializer
    queryset = Fechas.objects

    def get(self,request,format=None):
        fechas = self.queryset.all()
        serializer = self.serializer_class(fechas,many=True)
        return Response(serializer.data)

class FechasDetail(APIView):
    serializer_class = FechaSerializer
    queryset = Fechas.objects

    def get(self,request,pk,format=None):
        fechas = self.queryset.get(pk)
        serializer = self.serializer_class(fechas)
        return Response(serializer.data)

class FechasByCuil(APIView):
    serializer_class = FechaSerializer
    queryset = Fechas.objects

    def get(self,request,cuil,format=None):
        fechas = self.queryset.filter(user=cuil)
        serializer = self.serializer_class(fechas,many=True)
        return Response(serializer.data)


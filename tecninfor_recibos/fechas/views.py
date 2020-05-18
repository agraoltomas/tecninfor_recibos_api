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
        
        day = request.query_params.get("day",None)
        month = request.query_params.get("month",None)
        year = request.query_params.get("year",None)
        fechas = self.queryset
        if day:
            fechas = fechas.filter(fecha__day=day)
        if month:
            fechas = fechas.filter(fecha__month=month)
        if year:
            fechas = fechas.filter(fecha__year=year)

        serializer = self.serializer_class(fechas.all(),many=True)

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


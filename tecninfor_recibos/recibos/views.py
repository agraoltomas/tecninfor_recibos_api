from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tecninfor_recibos.models import Recibos
from recibos.serializers import ReciboDataSerializer,ReciboBytesSerializer
# Create your views here.


class RecibosList(APIView):
    serializer_class = ReciboDataSerializer
    queryset = Recibos.objects

    def get(self,request,format=None):
        recibos = self.queryset.only("cuil","periodo","tipo")
        serializer = self.serializer_class(recibos,many=True)
        return Response(serializer.data)

class RecibosDetail(APIView):
    serializer_class = ReciboDataSerializer
    queryset = Recibos.objects

    def get(self,request,pk,format=None):
        recibo = self.queryset.get(id=pk)
        serializer = self.serializer_class(recibo)
        return Response(serializer.data)


class RecibosByCuil(APIView):
    serializer_class = ReciboDataSerializer
    queryset = Recibos.objects

    def get(self,request,cuil,format=None):
        recibos = self.queryset.filter(cuil=cuil).order_by('-periodo').only("cuil","periodo","tipo")
        serializer = self.serializer_class(recibos,many=True)
        return Response(serializer.data)

class RecibosByCuilCount(APIView):
    queryset = Recibos.objects

    def get(self,request,cuil,format=None):
        recibos = self.queryset.filter(cuil=cuil).count()
        return Response({'count':recibos},status=status.HTTP_200_OK)

class RecibosByteDetail(APIView):
    queryset = Recibos.objects
    serializer_class = ReciboBytesSerializer
    def get(self,request,pk,format=None):
        recibo = self.queryset.get(id=pk)

        recibo_data = {
            'id':recibo.id,
            'cuil':recibo.cuil.cuil,
            'bytes':recibo.bytes.decode()
        }

        return Response(recibo_data)
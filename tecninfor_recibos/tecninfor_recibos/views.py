from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from tecninfor_recibos.serializers import EmpleadoSerializer
from tecninfor_recibos.models import Empleados


class EmpleadoList(APIView):

    serializer_class = EmpleadoSerializer
    queryset = Empleados.objects
    def get(self,request,format=None):
        serializer = self.serializer_class(self.queryset.all(),many=True)
        return Response(serializer.data)

class EmpleadoDetail(APIView):

    serializer_class = EmpleadoSerializer
    queryset = Empleados.objects
    def get(self,request,cuil,format=None):
        empleado = self.queryset.filter(cuil=cuil).first()
        serializer = self.serializer_class(empleado)
        return Response(serializer.data)


@api_view(['GET'])
def api_root(request):
    return Response(data={
        'empleados':reverse('empleados',request=request),
    })

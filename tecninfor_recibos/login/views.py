from rest_framework.views import APIView
from rest_framework.response import Response
from tecninfor_recibos.models import Login
from login.serializer import LoginSerializer

class LoginEmpleado(APIView):
    class_serializer = LoginSerializer
    queryset = Login.objects

    def get(self,request,cuil,format=True):
        login_data = self.queryset.filter(cuil=cuil).first()
        serializer = self.class_serializer(login_data)
        return Response(serializer.data)

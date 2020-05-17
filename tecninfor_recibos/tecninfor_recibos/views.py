from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import redirect

@api_view(['GET'])
def api_root(request):
    return Response(data={
        'empleados':reverse('empleados',request=request),
    })

@api_view(['GET'])
def redirect_root(request):
    return redirect('/api/v1/resources')

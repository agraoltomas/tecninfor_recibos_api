"""tecninfor_recibos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

import tecninfor_recibos.views as trecibos_views
import recibos.views as recibos_views

urlpatterns = [
    path('api/v1/resources/admin/', admin.site.urls),
    path('api/v1/resources/empleado/',trecibos_views.EmpleadoList.as_view(),name="empleados"),
    path('api/v1/resources/empleado/<int:cuil>',trecibos_views.EmpleadoDetail.as_view(),name="empleado"),
    path('api/v1/resources/empleado/<int:cuil>/recibos',recibos_views.RecibosByCuil.as_view(),name="empleado_recibos"),
    path('recibos/',include("recibos.urls")),
    path('api/v1/resources/',trecibos_views.api_root,name="apiroot"),
]

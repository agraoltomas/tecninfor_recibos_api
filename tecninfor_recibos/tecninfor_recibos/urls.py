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
import fechas.views as fechas_views

BASIC_URL = "api/v1/resources/"

urlpatterns = [
    path('',trecibos_views.redirect_root,name="root_redirect"),
    path(f'{BASIC_URL}',trecibos_views.api_root,name="apiroot"),
    path(f'{BASIC_URL}empleado/',include('empleado.urls')),
    path(f'{BASIC_URL}admin/', admin.site.urls),
    path(f'{BASIC_URL}recibos/',include("recibos.urls")),
    path(f'{BASIC_URL}fechas/',include("fechas.urls")),
    path(f'{BASIC_URL}login/',include('login.urls')),

]

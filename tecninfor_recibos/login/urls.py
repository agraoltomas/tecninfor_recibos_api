from django.urls import path
from login import views as login_views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('',obtain_auth_token,name="login"),
    path('<int:cuil>',login_views.LoginEmpleado.as_view(),name='login_empleado'),
]

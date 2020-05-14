from django.urls import path
from login import views as login_views

urlpatterns = [
    path('<int:cuil>',login_views.LoginEmpleado.as_view(),name='login_empleado'),
]

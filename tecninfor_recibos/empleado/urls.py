from django.urls import path
import recibos.views as recibos_views
import fechas.views as fechas_views
import empleado.views as empleado_views

urlpatterns = [

    path('',empleado_views.EmpleadoList.as_view(),name="empleados"),
    path('<int:cuil>',empleado_views.EmpleadoDetail.as_view(),name="empleado"),
    path('<int:cuil>/recibos',recibos_views.RecibosByCuil.as_view(),name="empleado_recibos"),
    path('<int:cuil>/recibos/count',recibos_views.RecibosByCuilCount.as_view(),name="empleado_recibos_count"),
    path('<int:cuil>/fechas',fechas_views.FechasByCuil.as_view(),name="empleado_fechas"),

]

from django.urls import path
import fechas.views as views
urlpatterns = [
    path('',views.FechasList.as_view(),name="fechas"),
    path('<int:pk>/',views.FechasDetail.as_view(),name="fecha"),
]

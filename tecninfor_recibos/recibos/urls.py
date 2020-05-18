from django.urls import path
import recibos.views as recibos_views
urlpatterns = [
    path('',recibos_views.RecibosList.as_view(),name="recibos"),
    path('<int:pk>',recibos_views.RecibosDetail.as_view(),name="recibo"),
    path('<int:pk>/file',recibos_views.RecibosByteDetail.as_view(),name="recibo_file")


]

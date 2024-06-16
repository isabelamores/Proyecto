from django.urls import path
from . import views

urlpatterns = [
    path ('',views.index),
    path ('registro/',views.registro),
    path ('editar/',views.editar),
    path ('informe/',views.informe),
]
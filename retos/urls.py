from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:mes>", views.retos_mensuales_por_numero),
    path("<str:mes>", views.retos_mensuales, name="retos-mensuales")
]

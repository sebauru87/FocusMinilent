from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ubicacion/", views.location, name="location"),
    path("lab", views.lab, name="lab"),
]
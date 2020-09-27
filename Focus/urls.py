from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ubicacion/", views.location, name="location"),
    path("lab", views.lab, name="lab"),
    path("ubicacion/submit_form", views.submit_form, name="submit_form"),
    path("lentescontacto", views.lentescontacto, name="lentescontacto"),
]
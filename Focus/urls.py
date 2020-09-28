from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("lab", views.lab, name="lab"),
    path("contact/submit_form", views.submit_form, name="submit_form"),
    path("lentescontacto", views.lentescontacto, name="lentescontacto"),
]
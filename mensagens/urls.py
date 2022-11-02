from django.urls import path
from . import views

app_name = "mensagens"


urlpatterns = [
    path("uso/", views.form_solicitaruso, name="solicitaruso"),
    path("erro/", views.form_informarerro, name="informarerro"),

]
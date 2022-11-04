from django.urls import path
from . import views

app_name = "mensagens"


urlpatterns = [
    path("uso/<slug:slug>/", views.form_solicitaruso, name="solicitaruso"),
    path("erro/<slug:slug>/", views.form_informarerro, name="informarerro"),
    
]
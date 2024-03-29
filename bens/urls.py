from django.urls import path
from .views import ProductDetailView, ProductListView
from . import views

app_name = "bens"

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("filtros/", views.filtros_list, name="filtros"),
    path("totais/", views.totais_list, name="totais_bens"),
    path("editar/<slug:slug>/", views.editBem, name="editbem"),
    path("imagem/<slug:slug>/", views.imagemBem, name="imagembem"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    path("porsetor/<slug:slug>/", ProductListView.as_view(), name="list_by_category"),
    
]
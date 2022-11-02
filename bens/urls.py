from django.urls import path
from .views import ProductDetailView, ProductListView
from . import views

app_name = "bens"

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("editar/<slug:slug>/", views.editBem, name="editbem"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    path("categoria/<slug:slug>/", ProductListView.as_view(), name="list_by_category"),
    
]
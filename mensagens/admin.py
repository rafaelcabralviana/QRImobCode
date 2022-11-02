from django.contrib import admin
from mensagens.models import Uso, Erro

# Register your models here.
@admin.register(Uso)
class UsoAdmin(admin.ModelAdmin):
    list_display = ["bem","email", "motivo"]


@admin.register(Erro)
class ErroAdmin(admin.ModelAdmin):
    list_display = ["bem","email"]
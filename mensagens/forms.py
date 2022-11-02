from django import forms
from .models import Uso, Erro


class UsoForm(forms.ModelForm):
    class Meta:
        model = Uso
        fields = "__all__"

class ErroForm(forms.ModelForm):
    class Meta:
        model = Erro
        fields = "__all__"
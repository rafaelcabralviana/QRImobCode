from django import forms
from .models import Uso, Erro


class UsoForm(forms.ModelForm):
    class Meta:
        model = Uso
        fields = ['bem', 'email', 'motivo', 'mensagem', 'image']

    

class ErroForm(forms.ModelForm):
    class Meta:
        model = Erro
        fields = "__all__"
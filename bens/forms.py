from django import forms
from bens.models import Product

class ImagemForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["categoria"].disabled = True
        self.fields["codigo"].disabled = True
        self.fields["descricao"].disabled = True
        self.fields["tag"].disabled = True
        self.fields["setor"].disabled = True
        self.fields["local"].disabled = True
        self.fields["responsavel"].disabled = True
        self.fields["data_inicial"].disabled = True
        self.fields["data_final"].disabled = True
        self.fields["is_available"].disabled = True

class BensForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
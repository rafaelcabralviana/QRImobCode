from django import forms
from bens.models import Product

class BensForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
    
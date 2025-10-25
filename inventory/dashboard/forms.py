from django import forms
from .models import product


class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name','category','Quantity']

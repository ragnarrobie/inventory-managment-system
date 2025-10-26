from django import forms
from .models import product,Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name','category','Quantity']
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','order_quantity']
from django import forms
from .models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'description','product_image1', 'short_description', 'product_image2', 'price']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False)
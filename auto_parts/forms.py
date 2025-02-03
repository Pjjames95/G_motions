from django import forms
from .models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'description','product_image_url', 'short_description', 'product_image2_url', 'price']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False)
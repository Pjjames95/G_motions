from django.contrib import admin
from .models import Products
from .forms import ProductsForm

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    form = ProductsForm
    list_display = ('product_name', 'price', 'description', 'product_image1', 'short_description', 'product_image2')

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            form.save()
            self.message_user(request, 'Product updated successfully')




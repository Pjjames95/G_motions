from django.db import models

from user_authentication.models import CustomUser


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    short_description = models.CharField(max_length=255)
    product_image1 = models.ImageField(upload_to='products_images/')
    product_image2 = models.ImageField(upload_to='products_images/')


    def __str__(self):
        return self.product_name

class Cart(models.Model):
    CustomUser = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, through='CartItem')


    def __str__(self):
        return f"Cart for {self.CustomUser.username}"

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"{self.quantity}  {self.product.product_name}"



from django.db import models
from django.utils import timezone

class Order(models.Model):
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')
    payment_method = models.CharField(max_length=50, default='Pay on Delivery')
    order_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"Order #{self.id} - {self.status}"
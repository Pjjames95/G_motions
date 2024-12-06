from django import forms
from .import models

class PaymentForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ('phone', 'address', 'total_price', 'status', 'payment_method')
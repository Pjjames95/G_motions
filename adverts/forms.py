from django import forms
from .models import Cars, AdminMessage


class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['car_name', 'car_make', 'car_model', 'property_1', 'property_2', 'description', 'car_image_url', 'short_description', 'car_image2_url']

    image_url = forms.URLField(label='Image URL', required=True)


class ContactForm(forms.ModelForm):
    class Meta:
        model = AdminMessage
        fields = ['name', 'email', 'message']

class AdminMessageForm(forms.ModelForm):
    class Meta:
        model = AdminMessage
        fields = ['name', 'email', 'message']
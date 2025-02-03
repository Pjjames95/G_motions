from django import forms
from .models import Garage_services, ComplainMessage

class GarageForms(forms.ModelForm):
    class Meta:
        model = Garage_services
        fields = ['garage_name', 'garage_location', 'garage_image_url', 'garage_contacts']


class ComplainMessageForm(forms.ModelForm):
    class Meta:
        model = ComplainMessage
        fields = ['message', 'email']
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Enter your complaint here...', 'rows': 5}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email address'}),
        }
        labels = {
            'message': 'Complaint Message',
            'email': 'Your Email',
        }
        help_texts = {
            'email':'We will only use this to contact you if necessary.',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # You can add custom email validation logic here if needed.
        if not email:
            raise forms.ValidationError("Email is required.")
        return email

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message:
            raise forms.ValidationError("Message cannot be empty.")
        return message

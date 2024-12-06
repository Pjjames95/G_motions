from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'accept_terms', 'completed']
        labels = {
            'accept_terms': 'I agree to the Terms and Conditions',
        }

class CustomUserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    alternative_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Bio'}))
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'alternative_password', 'profile_image', 'bio', 'completed']

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'alternative_password', 'profile_image', 'bio', 'completed']
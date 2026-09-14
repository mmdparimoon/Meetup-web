from django import forms
from .models import Participant

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
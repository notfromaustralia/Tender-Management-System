from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=40,)
    company_name = forms.CharField(max_length=100,)
    mobile_number = forms.CharField(max_length=20,)
    address = forms.CharField(max_length=100,)

    class Meta:
        model = User
        fields = ('username', 'email', 'company_name', 'mobile_number', 'address', 'password1', 'password2')
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None
        }

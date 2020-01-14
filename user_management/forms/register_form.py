from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=60, min_length=6, label='Email Address')
    fullname = forms.CharField(max_length=60, required=True, label='Full Name')

    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'password1', 'password2']

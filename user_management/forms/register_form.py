from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from orient_advances.models import Section


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=60, min_length=6, label='Email Address')
    fullname = forms.CharField(max_length=60, required=True, label='Full Name')
    employee_id = forms.IntegerField()
    is_boss = forms.BooleanField(label='Head of the Department')
    # section = forms.ChoiceField(choices=(),required=True,label='Department')


    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'password1', 'password2', 'employee_id', 'is_boss']

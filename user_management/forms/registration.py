from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_management.models import Account
from orient_advances.models import Section

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60,help_text='Required, add a valid email address.', required=True)
    fullname = forms.CharField(max_length=60, required=True, label='Full Name')
    employee_id = forms.CharField(max_length=10, required=True, label='Employee ID')
    image = forms.ImageField(allow_empty_file=True,required=False,label='Profile Image')
    is_boss = forms.BooleanField(label='Head of the Department',required=False)
    section = forms.ModelChoiceField(queryset=Section.objects.all(),required=True,label='Department')

    class Meta:
        model = Account
        fields= ['email','username','fullname','image','password1','password2','employee_id','is_boss','section']
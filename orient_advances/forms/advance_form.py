from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from user_management.models import Account
from orient_advances.models import Advance
from orient_project import settings

class AdvanceForm(ModelForm):
    # emplyee = forms.ModelChoiceField(queryset=Account.objects.all(),limit_choices_to=)
    amount = forms.FloatField(max_value=10000,min_value=100,help_text='Amount should be in LE')
    request_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,label='Advance Date')

    class Meta:
        model = Advance
        fields= ['amount','request_date']
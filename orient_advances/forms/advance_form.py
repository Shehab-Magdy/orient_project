from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_management.models import Account
from orient_advances.models import Advance
from orient_project import settings


class AdvanceForm(forms.ModelForm):
    # emplyee = forms.ModelChoiceField(queryset=Account.objects.all(),limit_choices_to=)
    amount = forms.DecimalField(max_value=10000, min_value=50, help_text='Amount should be between 50 LE to 10000 LE')
    request_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, label='Advance Date', help_text='Date formate DD-MM-YYYY')

    class Meta:
        model = Advance
        fields = ['amount', 'request_date']

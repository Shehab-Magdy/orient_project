from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_management.models import Account
# from orient_other.models import otherForm
from orient_project import settings
from orient_advances.models import Section, other


class otherForm(forms.ModelForm):
    # emplyee = forms.ModelChoiceField(queryset=Account.objects.all(),limit_choices_to=)
    amount = forms.DecimalField(max_value=10000, min_value=50, help_text='Amount should be between 50 LE to 10000 LE')
    request_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, label='Advance Date', help_text='Date formate DD-MM-YYYY')
    description = forms.CharField(widget=forms.Textarea)
    section = forms.ModelChoiceField(queryset=Section.objects.all(),required=True,label='Department')

    class Meta:
        model = other
        fields = ['amount', 'request_date','section']
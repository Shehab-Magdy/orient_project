from django import forms
from orient_advances.models import Expens


class ExpensForm(forms.ModelForm):
    name = forms.CharField(required=True, label='Expense Name')

    class Meta:
        model = Expens
        fields = ['name']

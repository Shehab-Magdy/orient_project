from django import forms
from orient_advances.models import Section


class SectionForm(forms.ModelForm):
    name = forms.CharField(required=True, label='Department Name')

    class Meta:
        model = Section
        fields = ['name']

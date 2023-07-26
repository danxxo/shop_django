from typing import Any, Dict
from django import forms

class DateForm(forms.Form):

    DATE_CHOICES = (
        ('0', 'no filter'),
        ('1', 'last week'),
        ('2', 'last month'),
        ('3', 'last year'),
        ('4', 'All time')
    )

    start = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    end = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    choice = forms.ChoiceField(choices=DATE_CHOICES, required=False)


    def clean(self):
        cd = super(DateForm, self).clean()

        choice = int(cd.get('choice'))
        start = cd.get('start')
        end = cd.get('end')

        if choice == 0:
            if not start and end:
                raise forms.ValidationError("validation error")
            if not end and start:
                raise forms.ValidationError("validation error")


        return super(DateForm, self).clean()
from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AgeCheck(UserCreationForm):
    date_of_birth = forms.DateField()

    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        age = (datetime.now() - dob).days/365
        if age < 18:
            raise forms.ValidationError('Must be 18 years old to enter')
        return dob


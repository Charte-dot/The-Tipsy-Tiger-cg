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


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

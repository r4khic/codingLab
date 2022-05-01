from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "second_name")


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()

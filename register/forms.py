from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):  # form to add more fields in the default register form that django provide us
    email = forms.EmailField()

    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2']

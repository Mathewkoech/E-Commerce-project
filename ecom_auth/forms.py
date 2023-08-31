from django import forms
import django
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = django.contrib.auth.models.User
        fields = ('username', 'email', 'password1', 'password2')
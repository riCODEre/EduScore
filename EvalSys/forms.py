from django import forms
from .models import *
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    class Meta:
        fields = [
            "first_name",
            "last_name",
            "username",
            "password"
            "Department",
            "BatchNumber",
            "Gender"
        ]

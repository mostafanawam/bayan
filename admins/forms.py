
from django import forms
from django.forms import Form


class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(required=True)


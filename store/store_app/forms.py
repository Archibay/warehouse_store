from django import forms
from .models import Order
from django.contrib.auth.models import User


class OrderForm(forms.Form):
    firs_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(help_text='Your address for delivery', required=True)

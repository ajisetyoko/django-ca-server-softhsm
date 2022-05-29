from django import forms
from django.forms import ModelForm
from .models import Key


class KeyForm(ModelForm):
    class Meta:
        model = Key
        fields = "__all__"

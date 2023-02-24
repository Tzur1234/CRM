from django import forms 
from .models import Lead, User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms.widgets import HiddenInput


class LeadModelForm(forms.ModelForm):
    # organization = forms.CharField(widget = forms.HiddenInput(), required = False, initial='Your name')
    # first_name = forms.CharField(initial='Your name')
    class Meta:
        model = Lead
        fields = '__all__'






class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        exclude = ['organization']

class UserCreationFormCustom(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
from django import forms 
from .models import Lead, User
from django.contrib.auth.forms import UserCreationForm, UsernameField


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
        exclude = ['organization']






class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        exclude = ['organization']

class UserCreationFormCustom(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
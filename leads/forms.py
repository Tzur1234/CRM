from django import forms 
from .models import Lead, User
from django.contrib.auth.forms import UserCreationForm, UsernameField


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'





class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()

class UserCreationFormCustom(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
from django.db import models
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

User = get_user_model()

class AgentModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username'] 
        
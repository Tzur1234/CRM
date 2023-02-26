from django import forms 
from .models import Lead, User, Agent, UserProfile , Category
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms.widgets import HiddenInput


class LeadModelForm(forms.ModelForm):
    # organization = forms.CharField(widget = forms.HiddenInput(), required = False, initial='Your name')
    # first_name = forms.CharField(initial='Your name')
    class Meta:
        model = Lead
        fields = '__all__'






class LeadForm(forms.ModelForm):
    organization = forms.ModelChoiceField(queryset=UserProfile.objects.none()) 
    class Meta:
        model = Lead
        exclude = ('organization',)
        # fields = '__all__'

    # pass extra information to the form 
    # def __init__(self, *args, **kwargs):    
    #     request = kwargs.pop("request")  
    #     organization = UserProfile.objects.filter(organization=request.user.userprofile)
    #     super(LeadForm, self).__init__(*args, **kwargs)
    #     self.fields["organization"].queryset = organization


class UserCreationFormCustom(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    # Filter agents
    def __init__(self, *args, **kwargs):    
        request = kwargs.pop("request")
        agent = Agent.objects.filter(organization=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agent


# Create form with categories from a specific organization 
class LeadCategoryForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.none())
    class Meta:
        model = Lead
        fields = ('category',)

    def __init__(self, *args, **kwargs):    
        organization = kwargs.pop("organization")
        categories = Category.objects.filter(organization=organization)
        super(LeadCategoryForm, self).__init__(*args, **kwargs)
        self.fields["category"].queryset = categories
    








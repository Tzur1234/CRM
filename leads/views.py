from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from .models import Lead, Agent, User, UserProfile, Category
from .forms import(
    LeadCategoryForm,
    LeadModelForm,
     UserCreationFormCustom,
     AssignAgentForm)   

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.signals import post_save, pre_save

from agents.mixins import OrganisorAndLoginRequiredMixin
 
class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationFormCustom

    def get_success_url(self):
        return reverse('login')

class LandingPageView(LoginRequiredMixin, TemplateView):
    template_name = 'leads/landing_page.html'

class ListPageView(LoginRequiredMixin, ListView):
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'
    model= Lead

    def get_queryset(self):       
        user = self.request.user
        if user.is_organisor:
            quertset =  Lead.objects.filter(organization=user.userprofile, agent__isnull=False) 
        else:
            quertset =  Lead.objects.filter(organization=user.agent.organization)    
            quertset = quertset.filter(agent__user=user,agent__isnull=False)
        
        return quertset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        user = self.request.user
        queryset = Lead.objects.filter(
                    organization=user.userprofile,
                    agent__isnull=True
                    )
        context.update({'unassigned_leads':queryset})
        return context

class LeadDetail(LoginRequiredMixin, DetailView):
    template_name = 'leads/lead_detail.html'
    
    def get_queryset(self):       
        user = self.request.user
        if user.is_organisor:
            quertset =  Lead.objects.filter(organization=user.userprofile)
        else:
            quertset =  Lead.objects.filter(organization=user.agent.organization)    
            quertset = queryset.filter(agent__user=user)  
        return quertset

class CreatLeadView(OrganisorAndLoginRequiredMixin, CreateView):
    template_name = 'leads/lead_create.html'
    model = Lead
    form_class = LeadModelForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs(**kwargs)  
        kwargs.update({"request": self.request})
        return kwargs

    def form_valid(self, form):

        lead = form.save(commit=False)
        lead.save()

        # Send EMAIL
        send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com']
    )

        return super().form_valid(form)

    def get_queryset(self):       
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile, agent__isnull=False)
        
    def get_success_url(self):
        # print("Success !")
        return reverse('leads:leads')

class UpdateLead(OrganisorAndLoginRequiredMixin, UpdateView, FormView):
    model = Lead
    form_class = LeadModelForm
    template_name = 'leads/lead_update.html'

    def get_success_url(self):
        return reverse('leads:leads')
    
    def get_queryset(self):       
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs(**kwargs)  
        kwargs.update({"request": self.request})
        return kwargs
 
class DeleteLead(OrganisorAndLoginRequiredMixin,DeleteView):
     # specify the model you want to use
    model = Lead   
    # url to redirect after successfully
    def get_success_url(self):
        return reverse('leads:leads')    
    
    def get_queryset(self):       
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)

class AssignAgentView(OrganisorAndLoginRequiredMixin, FormView):
    template_name='leads/assign_agent.html'
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({"request": self.request})
        return kwargs

    def get_success_url(self):
        return reverse('leads:leads')

    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()

        return super().form_valid(form)

class CategoryListView(LoginRequiredMixin, ListView):
    template_name: 'leads/category_list.html'
    context_object_name = "category_list"    

    def get_queryset(self, **kwargs):
        user = self.request.user

        if user.is_organisor:
            queryset = Category.objects.filter(organization = user.userprofile)
        else:
            queryset = Category.objects.filter(organization = user.agent.organization)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # get the number of leads with category field == NULL
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organization=user.userprofile, category__isnull=True)
        else:
            queryset = Lead.objects.filter(organization = user.agent.organization,category__isnull=True)

        context["unassigned_leads_count"] = queryset.count() 
        return context
    
class CategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'leads/category_detail.html'
    context_object_name = 'category'

    def get_queryset(self, **kwargs):
        user = self.request.user

        if user.is_organisor:
            queryset = Category.objects.filter(organization = user.userprofile)
        else:
            queryset = Category.objects.filter(organization = user.agent.organization)

        return queryset

    # Add all the leads form the selected Category
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch all leads with the same Showed category
        leads = Lead.objects.filter(category=self.get_object())
        leads = self.get_object().lead_set.all()

        print(leads)

        context.update({
            'leads':leads
        })

        return context

class LeadCategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'leads/lead_category_update.html'
    form_class = LeadCategoryForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs(**kwargs)

        user = self.request.user
        if user.is_organisor:
            organization = user.userprofile
        else:
            organization = user.agent.organization
        
    
        kwargs.update({"organization": organization})
        return kwargs
 
    def get_queryset(self):       
        user = self.request.user
        if user.is_organisor:
            quertset =  Lead.objects.filter(organization=user.userprofile)
        else:
            quertset =  Lead.objects.filter(organization=user.agent.organization)    
            quertset = queryset.filter(agent__user=user)  
        return quertset

    
    def get_success_url(self):
        return reverse('leads:lead_detail', args=[self.get_object().id])





            


















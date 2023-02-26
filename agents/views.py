import random
from django.shortcuts import render, reverse
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import OrganisorAndLoginRequiredMixin
from .forms import AgentModelForm
from leads.models import Agent, User
from django.core.mail import send_mail

class AgentListView(OrganisorAndLoginRequiredMixin, ListView):
    template_name = 'agents/agents_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        # Bring me all the Agents that ther organization is the current user organization
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

class CreateAgentView(OrganisorAndLoginRequiredMixin,CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

  
    # Overide the form valid
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(f'{random.randint(0, 1000000)}')
        user.save()
        
        # Create new agent
        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile
        )

        # Send an emial to the agent 
        send_mail(
        'You are invited to be an angent',
        'You were added as an angent to the CRM system. Please come login to start working',
        'from@example.com',
        [f'{user.email}'],
        fail_silently=False,
        )
        return super(CreateAgentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('agents:agent-list')
    
class DeleteAgentView(OrganisorAndLoginRequiredMixin, DeleteView):
    template_name="agents/agent_confirm_delete.html"
    context_object_name = 'agent'

    def get_queryset(self):
        # Bring me all the Agents that ther organization is the current user organization
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_success_url(self):
        return reverse('agents:agent-list')

class DetailAgentView(OrganisorAndLoginRequiredMixin, DetailView):

    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'
    
    def get_queryset(self):
        # Bring me all the Agents that ther organization is the current user organization
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

class UpdateAgentView(OrganisorAndLoginRequiredMixin, UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm
    model = User

    def get_success_url(self):
        return reverse('agents:agent-list')

    
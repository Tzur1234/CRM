from django.shortcuts import render, reverse
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AgentModelForm
from leads.models import Agent

class AgentListView(LoginRequiredMixin, ListView):
    template_name = 'agents/agents_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        # Bring me all the Agents that ther organization is the current user organization
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

class CreateAgentView(CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent-list')

    # Overide the form valid
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(CreateAgentView, self).form_valid(form)

    

class DeleteAgentView(LoginRequiredMixin, DeleteView):
    template_name="agents/agent_confirm_delete.html"
    context_object_name = 'agent'

    def get_queryset(self):
        # Bring me all the Agents that ther organization is the current user organization
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_success_url(self):
        return reverse('agents:agent-list')


class DetailAgentView(LoginRequiredMixin, DetailView):

    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'
    
    def get_queryset(self):
        # Bring me all the Agents that ther organization is the current user organization
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

class UpdateAgentView(LoginRequiredMixin, UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent-list')

    def get_queryset(self):
        # Bring me all the Agents that ther organization is the current user organization
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
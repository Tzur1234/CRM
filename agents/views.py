from django.shortcuts import render, reverse
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent, UserProfile

class AgentListView(LoginRequiredMixin, ListView):
    template_name = 'agents/agents_list.html'
    model = Agent
    context_object_name = 'agents'

class CreateAgentView(CreateView):
    template_name = 'agents/agent_create.html'
    model = Agent
    fields = ('user',)


    # Overide the form valid
    def form_valid(self, form):
        # Add the organization field to Agent
        agent = form.save(commit=False)
        # agent.organization = self.request.user.userprofile
        agent.organization = UserProfile.objects.get(user=self.request.user)
        agent.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('agents:agent-list')


class DeleteAgentView(LoginRequiredMixin, DeleteView):
    model = Agent
    template_name="agents/agent_confirm_delete.html"
    context_object_name = 'agent'
    # success_url = reverse_lazy('agents:agent-list')

    def get_success_url(self):
        return reverse('agents:agent-list')


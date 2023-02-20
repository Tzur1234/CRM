from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Lead, Agent, User
from .forms import LeadForm

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request,'leads/lead_list.html', context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    print(lead)
    context = {
        'lead':lead
    }
    return render(request,'leads/lead_detail.html', context)

def create(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(first_name=first, last_name=last, age=age, agent=agent)

            return redirect(reverse('leads:leads'))
        
    return render(request, 'leads/lead_create.html', {'form':form})










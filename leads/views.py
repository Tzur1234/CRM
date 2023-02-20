from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Lead, Agent, User
from .forms import LeadModelForm
from django.views.generic import TemplateView, ListView, DetailView

def landing_page(request):
    return render(request, 'leads/landing_page.html')

class LandingPageView(TemplateView):
    template_name = 'leads/landing_page.html'


class ListPageView(ListView):
    template_name = 'leads/lead_list.html'
    model = Lead
    context_object_name = 'leads'



def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request,'leads/lead_list.html', context)


class LeadDetail(DetailView):
    template_name = 'leads/lead_detail.html'
    model = Lead

    # # Retrieve a specific object
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['lead'] = Lead.objects.get(pk=kwargs['pk'])
    #     return context


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    print(lead)
    context = {
        'lead':lead
    }
    return render(request,'leads/lead_detail.html', context)

# def create(request):
#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first = form.cleaned_data['first_name']
#             last = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(first_name=first, last_name=last, age=age, agent=agent)

#             return redirect(reverse('leads:leads'))
        
    # return render(request, 'leads/lead_create.html', {'form':form})


def create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST, request.FILES)
        if form.is_valid():
            # save as a new model
            form.save()
            return redirect(reverse('leads:leads'))
  
    return render(request, 'leads/lead_create.html', {'form':form})

def update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, request.FILES, instance=lead)
        if form.is_valid():
            # update the exsiting model
            form.save()
            return redirect(reverse('leads:lead_detail', args=[pk]))   
    context = {
        'lead':lead,
        'form':form
    }
    return render(request, 'leads/lead_update.html', context)


def delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect(reverse('leads:leads'))









from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from .models import Lead, Agent, User
from .forms import LeadModelForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

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


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    print(lead)
    context = {
        'lead':lead
    }
    return render(request,'leads/lead_detail.html', context)


class CreatLeadView(CreateView):
    template_name = 'leads/lead_create.html'
    model = Lead
    fields = ['first_name','last_name','age','phone','agent', 'email', 'image'] 

    def get_success_url(self):
        return reverse('leads:leads')


def create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST, request.FILES)
        if form.is_valid():
            # save as a new model
            form.save()
            return redirect(reverse('leads:leads'))
  
    return render(request, 'leads/lead_create.html', {'form':form})

class UpdateLead(UpdateView):
    model = Lead
    fields = '__all__'
    # form_class = LeadModelForm
    template_name = 'leads/lead_update.html'

    def get_success_url(self):
        return reverse('leads:leads')

# class UpdateLead(UpdateView):
#     # model = Lead
#     # fields = '__all__'
#     form_class = LeadModelForm
#     template_name = 'leads/lead_update.html'
#     def get_queryset(self):
#         return Lead.objects.all()
#         # return super().get_queryset()     
#     def get_success_url(self):
#         return reverse('leads:leads')


def update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, request.FILES, instance=lead)
        if form.is_valid():
            # update the exsiting model
            form.save()
            # return redirect(reverse('leads:lead_detail', args=[pk]))   
            return redirect(reverse('leads:leads'))   
    context = {
        'lead':lead,
        'form':form
    }
    return render(request, 'leads/lead_update.html', context)

class DeleteLead(DeleteView):
     # specify the model you want to use
    model = Lead   
    # url to redirect after successfully
    def get_success_url(self):
        return reverse('leads:leads')    


def delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect(reverse('leads:leads'))









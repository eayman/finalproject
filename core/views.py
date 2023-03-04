from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView 
from .models import *
from django.shortcuts import render, get_object_or_404,redirect, resolve_url
from .forms import *
class LandingPageView(TemplateView):
    template_name = "landing.html"

class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return resolve_url("core:lead-list")
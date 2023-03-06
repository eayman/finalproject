from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView 


class OffersPageView(TemplateView):
    template_name = "offers.html"
    
class Client_list(ListView):
    template_name ="clients/client_list.html"
    queryset = Client.objects.all()
    context_object_name = "client"
    
class Delete_client(DetailView):
    template_name = "clients/client_list.html"
    queryset = Client.objects.all()
    context_object_name = "client"
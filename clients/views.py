from django.shortcuts import render ,resolve_url
from .models import *
from .forms import *
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView 


class OffersPageView(TemplateView):
    template_name = "offers.html"
    
class Client_list(ListView):
    template_name ="clients/client_list.html"
    queryset = Client.objects.all()
    context_object_name = "client"
    

class Delete_client(DeleteView):
    template_name = "clients/client_delete.html"
    queryset = Client.objects.all()
    
    def get_success_url(self):
        return resolve_url("clients:client_list")
    
class ClientCreateView(CreateView):
    template_name = "clients/client_create.html"
    form_class = clientModelForm
    
    def get_success_url(self):
        return resolve_url("clients:client_list")
    
class ClientUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Client.objects.all()
    form_class = clientModelForm
    
    def get_success_url(self):
        return resolve_url("clients:client_list")
    

class ClientDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Client.objects.all()
    
    def get_success_url(self):
        return resolve_url("clients:client_list")
    
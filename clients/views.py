from django.shortcuts import render ,resolve_url
from .models import *
from .forms import *
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView 


class OffersPageView(TemplateView):
    template_name = "offers.html"
    
class Client_list(ListView):
    template_name ="clients/client-list.html"
    queryset = Client.objects.all()
    context_object_name = "client"
    

class Delete_client(DeleteView):
    template_name = "clients/client-delete.html"
    queryset = Client.objects.all()
    
    def get_success_url(self):
        return resolve_url("clients:client-list")
    
class ClientCreateView(CreateView):
    template_name = "clients/client-create.html"
    form_class = clientModelForm
    
    def get_success_url(self):
        return resolve_url("clients:client-list")
    
class ClientUpdateView(UpdateView):
    template_name = "clients/clients_update.html"
    queryset = Client.objects.all()
    form_class = clientModelForm
    
    def get_success_url(self):
        return resolve_url("clients:client-list")
    

class ClientDeleteView(DeleteView):
    template_name = "clients/client-delete.html"
    queryset = Client.objects.all()
    
    def get_success_url(self):
        return resolve_url("clients:client-list")
    
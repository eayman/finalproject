from django.shortcuts import render ,resolve_url
from .models import *
from .forms import *
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView 


class OffersPageView(TemplateView):
    template_name = "offers.html"
    
<<<<<<< HEAD
class Client_list(ListView):
    template_name ="clients/client-list.html"
    queryset = Client.objects.all()
    context_object_name = "client"
    

class Delete_client(DeleteView):
    template_name = "clients/client-delete.html"
    queryset = Client.objects.all()
    
    def get_success_url(self):
        return resolve_url("clients:client-list")
    
=======
class ClientListView(ListView):
    template_name ="clients/client_list.html"
    queryset = Client.objects.all()
    context_object_name = "client"
    
>>>>>>> 5697b6d3dcf7756ab597ef6a5f95f5acd227254d
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
class ClienDeletetView(DeleteView):
    template_name = "clients/client_delete.html"
    queryset = Client.objects.all()
    
    def get_success_url(self):
        return resolve_url("clients:client-list")
    
from django.shortcuts import render ,resolve_url
from .models import *
from .forms import *
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView 


class OffersPageView(TemplateView):
    template_name = "offers.html"

#############################################################
#################### Clients Views ##########################
#############################################################

class ClientListView(ListView):
    template_name ="clients/client_list.html"
    queryset = Client.objects.all()
    context_object_name = "client"
    
    
class ClientCreateView(CreateView):
    template_name = "clients/client_create.html"
    form_class = clientModelForm
    
    def get_success_url(self):
        return resolve_url("clients:client-list")
    
class ClientUpdateView(UpdateView):
    template_name = "clients/clients_update.html"
    queryset = Client.objects.all()
    form_class = clientModelForm
    
    def get_success_url(self):
        return resolve_url("clients:client-list")
    

class ClienDeletetView(DeleteView):
    template_name = "clients/client_delete.html"
    queryset = Client.objects.all()
    def get_success_url(self):
        return resolve_url("clients:client-list")
    


#############################################################
###################### Plans Views ##########################
#############################################################

class PlanListView(ListView):
    template_name ="subscriptions/sub_list.html"
    queryset = Subscription.objects.all()
    context_object_name = "plans"


#############################################################
#################### Subscriptions Views ####################
#############################################################

class SubListView(ListView):
    template_name ="subscriptions/sub_list.html"
    queryset = Subscription.objects.all()
    context_object_name = "subscriptions"

class SubCreateView(CreateView):
    template_name = "subscriptions/sub_create.html"
    form_class = SubModelForm
    
    def get_success_url(self):
        return resolve_url("clients:sub-list")
from django.shortcuts import render ,resolve_url
from .models import *
from .forms import *
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView ,DetailView


class OffersPageView(TemplateView):
    template_name = "offers.html"

#############################################################
#################### Clients Views ##########################
#############################################################

class ClientListView(ListView):
    template_name ="clients/client_list.html"
    queryset = Client.objects.all()
    context_object_name = "clients"
    
    
class ClientCreateView(CreateView):
    template_name = "clients/client_create.html"
    form_class = ClientModelForm
    
    def get_success_url(self):
        return resolve_url("clients:client-list")
    
class ClientUpdateView(UpdateView):
    template_name = "clients/client_update.html"
    queryset = Client.objects.all()
    form_class = ClientModelForm
    
    def get_success_url(self):
        return resolve_url("clients:client-list")
    

class ClientDeletetView(DeleteView):
    template_name = "clients/client_delete.html"
    queryset = Client.objects.all()
    def get_success_url(self):
        return resolve_url("clients:client-list")
    


#############################################################
###################### Plans Views ##########################
#############################################################

class PlanListView(ListView):
    template_name ="plans/plan_list.html"
    queryset = Plan.objects.all()
    context_object_name = "plans"

class PlanCreateView(CreateView):
    template_name = "plans/plan_create.html"
    form_class = PlanModelForm
    def get_success_url(self):
        return resolve_url("clients:plan-list")


class PlanUpdateView(UpdateView):
    template_name = "plans/plan_update.html"
    queryset = Plan.objects.all()
    form_class = PlanModelForm
    
    def get_success_url(self):
        return resolve_url("clients:plan-list")
    

class PlanDeletetView(DeleteView):
    template_name = "plans/plan_delete.html"
    queryset = Plan.objects.all()
    def get_success_url(self):
        return resolve_url("clients:plan-list")
    
    


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
    
    
class SubUpdateView(UpdateView):
    template_name = "subscriptions/sub_update.html"
    queryset = Subscription.objects.all()
    form_class =  SubModelForm
    
    def get_success_url(self):
        return resolve_url("clients:sub-list")
    

class SubDeletetView(DeleteView):
    template_name = "subscriptions/sub_delete.html"
    queryset =Subscription.objects.all()
    def get_success_url(self):
        return resolve_url("clients:sub-list")


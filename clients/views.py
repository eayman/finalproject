from django.shortcuts import render ,redirect, resolve_url ,HttpResponseRedirect
from .models import *
from .forms import *
from django.urls import reverse_lazy  
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView ,DetailView
from utils import PAGE_RESULTS, MyPaginator
from django.contrib.auth.mixins import LoginRequiredMixin


class OffersPageView(TemplateView):
    template_name = "offers.html"

#############################################################
#################### Clients Views ##########################
#############################################################

class ClientListView(LoginRequiredMixin, ListView):
    template_name ="clients/client_list.html"
    paginate_by = PAGE_RESULTS
    paginator_class = MyPaginator # We use our paginator class
    queryset = Client.objects.all()
    context_object_name = "clients"
    
    
class ClientCreateView(LoginRequiredMixin, CreateView):
    template_name = "clients/client_create.html"
    form_class = ClientModelForm
    
    def get_success_url(self):
            return resolve_url("clients:client-list")

    
class ClientUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "clients/client_update.html"
    queryset = Client.objects.all()
    form_class = ClientModelForm
    
    def get_success_url(self):
        return resolve_url("clients:client-list")
    

class ClientDeletetView(LoginRequiredMixin, DeleteView):
    template_name = "clients/client_delete.html"
    queryset = Client.objects.all()
    def get_success_url(self):
        return resolve_url("clients:client-list")
    


#############################################################
###################### Plans Views ##########################
#############################################################

class OffersListView( ListView):
    template_name ="offers.html"
    paginate_by = 4
    paginator_class = MyPaginator # We use our paginator class
    queryset = Plan.objects.all()
    context_object_name = "plans"

class PlanListView(LoginRequiredMixin, ListView):
    template_name ="plans/plan_list.html"
    paginate_by = PAGE_RESULTS
    paginator_class = MyPaginator # We use our paginator class
    queryset = Plan.objects.all()
    context_object_name = "plans"

class PlanCreateView(LoginRequiredMixin, CreateView):
    template_name = "plans/plan_create.html"
    form_class = PlanModelForm
    def get_success_url(self):
        return resolve_url("clients:plan-list")


class PlanUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "plans/plan_update.html"
    queryset = Plan.objects.all()
    form_class = PlanModelForm
    
    def get_success_url(self):
        return resolve_url("clients:plan-list")
    

class PlanDeletetView(LoginRequiredMixin, DeleteView):
    template_name = "plans/plan_delete.html"
    queryset = Plan.objects.all()
    def get_success_url(self):
        return resolve_url("clients:plan-list")
    
    


#############################################################
#################### Subscriptions Views ####################
#############################################################

class SubListView(LoginRequiredMixin, ListView):
    template_name ="subscriptions/sub_list.html"
    paginate_by = PAGE_RESULTS
    paginator_class = MyPaginator # We use our paginator class
    queryset = Subscription.objects.all()
    context_object_name = "subscriptions"

class SubCreateView(LoginRequiredMixin, CreateView):
    template_name = "subscriptions/sub_create.html"
    form_class = SubModelForm
    
    def get_success_url(self):
        return resolve_url("clients:sub-list")
    
    
class SubUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "subscriptions/sub_update.html"
    queryset = Subscription.objects.all()
    form_class =  SubModelForm
    
    def get_success_url(self):
        return resolve_url("clients:sub-list")
    

class SubDeletetView(LoginRequiredMixin, DeleteView):
    template_name = "subscriptions/sub_delete.html"
    queryset =Subscription.objects.all()
    def get_success_url(self):
        return resolve_url("clients:sub-list")


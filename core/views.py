from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView 
from .models import *
from django.shortcuts import render, get_object_or_404,redirect, resolve_url
from .forms import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.views import LoginView
from django.contrib import  messages

class LandingPageView(TemplateView):
    template_name = "landing.html"

class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Lead.objects.all()
        else:
            agent = get_object_or_404(Agent,user=self.request.user)
            return Lead.objects.filter(agent=agent)

class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return resolve_url("core:lead-list")
    
class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    
    def get_success_url(self):
        return resolve_url("core:lead-list")
    

class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return resolve_url("core:lead-list")
    

class AgentListView(ListView):
    template_name = "agents/agent_list.html"
    queryset = Agent.objects.all()
    context_object_name = "agents"

class AgentDetailView(DetailView):
    template_name = "agents/agent_profile.html"
    queryset = Agent.objects.all()
    context_object_name = "agent"



class AgentCreateView(CreateView):
    template_name = "agents/agent_create.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return resolve_url("core:agent-list")




class AgentUpdateView(UpdateView):
    template_name = "agents/agent_update.html"
    queryset = User.objects.all()
    form_class = CustomUserUpdateForm
    
    def get_success_url(self):
        return resolve_url("core:agent-list")
    

class AgentDeleteView(DeleteView):
    template_name = "agents/agent_delete.html"
    queryset = User.objects.all()

    def get_success_url(self):
        return resolve_url("core:agent-list")
    

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm



class ContactPageView(TemplateView):
    template_name = "contact.html"
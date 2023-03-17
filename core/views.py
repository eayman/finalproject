from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView 
from .models import *
from django.shortcuts import render, get_object_or_404,redirect, resolve_url ,HttpResponseRedirect
from .forms import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.views import LoginView
from django.contrib import  messages
from django.urls import reverse_lazy  
from django.contrib.auth.mixins import LoginRequiredMixin
from utils import MyPaginator, PAGE_RESULTS

class LandingPageView(TemplateView):
    template_name = "landing.html"

class LeadListView(LoginRequiredMixin,ListView):
    
    template_name = "leads/lead_list.html"
    paginate_by = PAGE_RESULTS
    paginator_class = MyPaginator # We use our paginator class
    
    def get_queryset(self):
        queryset = Lead.objects.all()
        return queryset
        
    context_object_name = "leads"

    

class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return resolve_url("core:lead-list")
    
class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    
    def get_success_url(self):
        return resolve_url("core:lead-list")
    

class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return resolve_url("core:lead-list")
    

class AgentListView(LoginRequiredMixin, ListView):
    template_name = "agents/agent_list.html"
    paginate_by = PAGE_RESULTS
    paginator_class = MyPaginator # We use our paginator class
    queryset = Agent.objects.all()
    context_object_name = "agents"

class AgentDetailView(LoginRequiredMixin, DetailView):
    template_name = "agents/agent_profile.html"
    queryset = Agent.objects.all()
    context_object_name = "agent"



class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = "agents/agent_create.html"
    form_class = CustomUserCreationForm
    
    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None
        form_class= CustomUserCreationForm (post_data, instance=request.user)
        
        if  form_class.is_valid():
            form_class.save()
            messages.success(request, 'Your Create agent successfully!')
            return HttpResponseRedirect(reverse_lazy('agents'))

        context = self.get_context_data(
                                            form_class= CustomUserCreationForm
                                        )
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs) 
        
    def get_success_url(self):
        return resolve_url("core:agent-list")
    
    



class AgentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "agents/agent_update.html"
    queryset = User.objects.all()
    form_class = CustomUserUpdateForm
    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None
        form_class= CustomUserUpdateForm (post_data, instance=request.user)
        
        if  form_class.is_valid():
            form_class.save()
            messages.success(request, 'Your Create agent successfully!')
            return HttpResponseRedirect(reverse_lazy('agents'))

        context = self.get_context_data(
                                            form_class= CustomUserUpdateForm
                                        )
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs) 
        
    def get_success_url(self):
        return resolve_url("core:agent-list")

class AgentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "agents/agent_delete.html"
    queryset = User.objects.all()

    def get_success_url(self):
        return resolve_url("core:agent-list")
    

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm



class ContactPageView(TemplateView):
    template_name = "contact.html"



def change_contacted_status(LoginRequiredMixin, request,pk):
    lead = get_object_or_404(Lead,id=pk)
    lead.is_contacted = not(lead.is_contacted)
    lead.save()
    return HttpResponse()
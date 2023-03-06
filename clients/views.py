from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView 


class OffersPageView(TemplateView):
    template_name = "offers.html"
    
class Client_list(TemplateView):
    template_name ="clients/client_list.html/"
    queryset = Client.objects.all()
    context_object_name = "client"

    def get_queryset(self):
            return Client.objects.all()
        
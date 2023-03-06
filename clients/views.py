from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView 


class OffersPageView(TemplateView):
    template_name = "offers.html"
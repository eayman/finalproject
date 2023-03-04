from django.urls import path
from core.views import *


urlpatterns = [
    path('',LeadListView.as_view(),name='lead-list'),
    path('lead-create',LeadCreateView.as_view(),name='lead-create'),
]

from django.urls import path
from core.views import *

app_name = "core"
urlpatterns = [
    path('',LeadListView.as_view(),name='lead-list'),
    path('lead-create',LeadCreateView.as_view(),name='lead-create'),
    path('<int:pk>/update/',LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/',LeadDeleteView.as_view(), name='lead-delete'),
    path('agents',AgentListView.as_view(),name='agent-list'),


]

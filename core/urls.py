from django.urls import path
from core.views import *

app_name = "core"
urlpatterns = [
    path('',LeadListView.as_view(),name='lead-list'),
    path('lead-create',LeadCreateView.as_view(),name='lead-create'),
    path('<int:pk>/update/',LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/lead-delete/',LeadDeleteView.as_view(), name='lead-delete'),
    path('agents',AgentListView.as_view(),name='agent-list'),
    path('agent-create',AgentCreateView.as_view(),name='agent-create'),
    path('<int:pk>/agent-delete/',AgentDeleteView.as_view(), name='agent-delete'),


]

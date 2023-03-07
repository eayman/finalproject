from django.urls import path
from core.views import *

app_name = "core"
urlpatterns = [
    #### Lead URLs
    path('leads/',LeadListView.as_view(),name='lead-list'),
    path('leads/lead-create',LeadCreateView.as_view(),name='lead-create'),
    path('leads/<int:pk>/update/',LeadUpdateView.as_view(), name='lead-update'),
    path('leads/<int:pk>/lead-delete/',LeadDeleteView.as_view(), name='lead-delete'),
    #### Agent URLs
    path('agents',AgentListView.as_view(),name='agent-list'),
    path('agents/<int:pk>/',AgentDetailView.as_view(), name='agent-profile'),
    path('agetns/agent-create',AgentCreateView.as_view(),name='agent-create'),
    path('agents/<int:pk>/update/',AgentUpdateView.as_view(), name='agent-update'),
    path('agetns/<int:pk>/agent-delete/',AgentDeleteView.as_view(), name='agent-delete'),
    

]

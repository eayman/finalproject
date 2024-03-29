from django.urls import path
from clients.views import *

app_name = "clients"
urlpatterns = [
    ################################ Clients URLs ###########################################
    path('clients', ClientListView.as_view(),name='client-list'),
    path('clients/create',ClientCreateView.as_view(),name='client-create'),
    path('clients/<int:pk>/update/',ClientUpdateView.as_view(), name='client-update'),
    path('clients/<int:pk>/delete/', ClientDeletetView.as_view(), name='client-delete'),

    ##################################### Plans URLs #########################################
    path('plans', PlanListView.as_view(),name='plan-list'),
    path('plans/create',PlanCreateView.as_view(),name='plan-create'),
    path('plans/<int:pk>/update/',PlanUpdateView.as_view(), name='plan-update'),
    path('plans/<int:pk>/delete/',PlanDeletetView.as_view(), name='plan-delete'),
    
    ################################ Subscriptions URLs ######################################
    path('subscriptions', SubListView.as_view(),name='sub-list'),
    path('subscriptions/create',SubCreateView.as_view(),name='sub-create'),
    path('subscriptions/<int:pk>/update/',SubUpdateView.as_view(), name='sub-update'),
    path('subscriptions/<int:pk>/delete/',SubDeletetView.as_view(), name='sub-delete'),
    
]
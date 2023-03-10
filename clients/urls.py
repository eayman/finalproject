from django.urls import path
from clients.views import *

app_name = "clients"
urlpatterns = [
    ################################ Clients URLs ###########################################
    path('clients', ClientListView.as_view(),name='client-list'),
    path('clients/create',ClientCreateView.as_view(),name='client-create'),
    path('clients/<int:pk>/update/',ClientUpdateView.as_view(), name='client-update'),
    path('clients/<int:pk>/delete/', ClienDeletetView.as_view(), name='client-delete'),

    ##################################### Plans URLs #########################################
    path('plans', PlanListView.as_view(),name='plan-list'),
    path('plans/create',planCreateView.as_view(),name='plan-create'),
    ################################ Subscriptions URLs ######################################
    path('subscriptions', SubListView.as_view(),name='sub-list'),
    path('subscriptions/create',SubCreateView.as_view(),name='sub-create'),

]
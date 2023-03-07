from django.urls import path
from clients.views import *

app_name = "clients"
urlpatterns = [
    path('clients/client-list', ClientListView.as_view(),name='client-list'),
    path('clients/client-create',ClientCreateView.as_view(),name='client-create'),
    path('clients/<int:pk>/client-update/',ClientUpdateView.as_view(), name='client-update'),
    path('clients/<int:pk>/client-delete/', ClienDeletetView.as_view(), name='client-delete') ,
     
]
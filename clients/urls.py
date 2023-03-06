from django.urls import path
from clients.views import *

app_name = "clients"
urlpatterns = [
    path ('clients/client_list', Client_list.as_view(),name='client_list'),
    path('clients/<int:pk>/client_delete/', Delete_client.as_view(), name='client_delete') ,
    path('clients/client_create',ClientCreateView.as_view(),name='client_create'),
    path('clients/<int:pk>/client_update/',ClientUpdateView.as_view(), name='client_update'),
     
     
]
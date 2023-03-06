from django.urls import path
from clients.views import *

app_name = "clients"
urlpatterns = [
    path ('clients/client-list', Client_list.as_view(),name='client-list'),
    path('clients/client-create',ClientCreateView.as_view(),name='client-create'),
    path('clients/<int:pk>/client_update/',ClientUpdateView.as_view(), name='client-update'),
    path('clients/<int:pk>/client-delete/', Delete_client.as_view(), name='client-delete') ,
     
]
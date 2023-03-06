from django.urls import path
from clients.views import *

app_name = "clients"
urlpatterns = [
    path ('clients/client_list', Client_list.as_view(),name='client_list'),
    path('clients/<int:pk>/delete_client/',Delete_client.as_view(), name='delete_client')    
]
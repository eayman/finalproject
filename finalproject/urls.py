from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from core.views import *
from clients.views import *
from django.contrib.auth.views import LoginView,LogoutView, PasswordChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LandingPageView.as_view(),name='landing-page'),
    path('contact-us',ContactPageView.as_view(),name='contact-us'),
    path('offers',OffersPageView.as_view(),name='offers'),
    path('',include("core.urls",namespace="core")),
    path('clients/',include("clients.urls",namespace="clients")),
    #### Auth URLs
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/',PasswordChangeView.as_view(),name='password_change')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
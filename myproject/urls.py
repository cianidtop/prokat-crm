"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authViews
from client import views as clientViews
from ride import views as rideViews
from tech import views as techViews

urlpatterns = [
    path('exit', authViews.LogoutView.as_view(template_name='main/exit.html'), name='exit'),
    path('auth', authViews.LoginView.as_view(template_name='main/auth.html'), name='auth'),
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('client/', clientViews.client, name='client'),
    path('search_client/', clientViews.SearchResultsView.as_view(), name='client_search'),
    path('tech/', techViews.tech, name='tech'),
    path('search_ride/', rideViews.SearchResultsView.as_view(), name='ride_search'),
    path('ride/', rideViews.ride, name='ride'),
    path('search_tech/', techViews.SearchResultsView.as_view(), name='tech_search'),
    path('clientnew/', clientViews.clientnew, name='clientnew'),
    path('ridenew/', rideViews.ridenew, name='ridenew'),
    path('technew/', techViews.technew, name='technew'),
    path('tech/<int:pk>/edit', techViews.tech_edit, name='tech_edit'),
    path('tech/<int:pk>/', techViews.tech_detail, name='tech_detail'),
    path('ride/<int:pk>/', rideViews.ride_detail, name='ride_detail'),
    path('ride/<int:pk>/edit', rideViews.ride_edit, name='ride_edit'),
    path('client/<int:pk>/', clientViews.client_detail, name='client_detail'),
    path('client/<int:pk>/edit', clientViews.client_edit, name='client_edit'),
    path('cash/', rideViews.cash, name='cash'),
]

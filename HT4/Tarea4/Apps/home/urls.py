"""
URL configuration for Tarea4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from Apps.home import views
from .views import HomeView
##from .views import EstudiantesView
##from .views import AdminView
##from .views import AcercaView
from Apps.administradores.views import AcercaView, RegistroView
import Apps.administradores.views

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='homeapp'),
    path('administradores/', Apps.administradores.views.ListarAdministradores, name='adminapp'),
    path('estudiantes/', Apps.administradores.views.ListarEstudiantes, name='estudiantesapp'),
    path('publicaciones/', Apps.administradores.views.ListarPublicaciones, name='publiapp'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('acerca/', AcercaView.as_view(), name='acercasapp'),
]
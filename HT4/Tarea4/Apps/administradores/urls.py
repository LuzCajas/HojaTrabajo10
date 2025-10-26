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
from Apps.administradores import views
from .views import AcercaView
from .views import CrearEstudiante, CrearAdmin, CrearPublicaion, EditarEstudiante, EditarAdmin, EditarPublicacion, RegistroView
from Apps.home.views import HomeView


app_name = 'administradores'

urlpatterns = [
    path('administ/', views.ListarAdministradores, name='adminapp'),
    path('crear_autorizador/', CrearAdmin.as_view(), name='crearadminapp'),
    path('editar_admin/<int:pk>', EditarAdmin.as_view(), name='editaradminapp'),
    path('ver_admin/<int:pk>', views.VerAdmin.as_view(), name='veradminapp'),
    path('estudiantes/', views.ListarEstudiantes, name='estudiantesapp'),
    path('crear_estudiante/', CrearEstudiante.as_view(), name='crearestapp'),
    path('editar_estudiante/<int:pk>', EditarEstudiante.as_view(), name='editarestapp'),
    path('ver_estudiante/<int:pk>', views.VerEstudiante.as_view(), name='verestapp'),
    path('acerca/', AcercaView.as_view(), name='acercasapp'),
    path('publicaciones/', views.ListarPublicaciones, name='publiapp'),
    path('crear_publicacion/', CrearPublicaion.as_view(), name='crearpubliapp'),
    path('editar_publicacion/<int:pk>', EditarPublicacion.as_view(), name='editarpubliapp'),
    path('ver_publicacion/<int:pk>', views.VerPublicacion.as_view(), name='verpubliapp'),
    path('registro/', RegistroView.as_view(), name='registroapp'),
    path('', HomeView.as_view(), name='homeapp'),
]
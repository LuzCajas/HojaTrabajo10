from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from .models import Administrador, Estudiante, Publicacion, Usuario
from .forms import EstudianteForm, AdministradorForm, PublicacionForm, RegistroForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.

@login_required(login_url='home:login')
def ListarEstudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes})

@login_required(login_url='home:login')
def ListarAdministradores(request):
    administradores = Administrador.objects.all()
    return render(request, 'admin.html', {'administradores': administradores})

@login_required(login_url='home:login')
def ListarPublicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'publicaciones.html', {'publicaciones': publicaciones})

@login_required(login_url='home:login')
def ListarVer(request):
    return render(request, 'home:acercasapp')

class AcercaView(TemplateView):
    template_name = 'acerca.html'

class PubliView(TemplateView):
    template_name = 'publicaciones.html'

class CrearEstudiante(CreateView):
    template_name = 'crear_est.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('administradores:estudiantesapp')

class EditarEstudiante(UpdateView):
    template_name = 'editar_est.html'
    form_class = EstudianteForm
    model = Estudiante
    success_url = reverse_lazy('administradores:estudiantesapp')

class VerEstudiante(DetailView):
    template_name = 'ver_est.html'
    model = Estudiante

class CrearAdmin(CreateView):
    template_name = 'crear_admin.html'
    form_class = AdministradorForm
    success_url = reverse_lazy('administradores:adminapp')

class EditarAdmin(UpdateView):
    template_name = 'editar_admin.html'
    form_class = AdministradorForm
    model = Administrador   
    success_url = reverse_lazy('administradores:adminapp')

class VerAdmin(DetailView):
    template_name = 'ver_admin.html'
    form_class = AdministradorForm
    model = Administrador
    success_url = reverse_lazy('administradores:adminapp')

class CrearPublicaion(CreateView):
    template_name = 'crear_publi.html'
    form_class = PublicacionForm
    success_url = reverse_lazy('administradores:publiapp')

class EditarPublicacion(UpdateView):
    template_name = 'editar_publi.html'
    form_class = PublicacionForm
    model = Publicacion
    success_url = reverse_lazy('administradores:publiapp')

class VerPublicacion(DetailView):
    template_name = 'ver_publi.html'
    form_class = PublicacionForm
    model = Publicacion
    success_url = reverse_lazy('administradores:publiapp')

class RegistroView(CreateView):
    template_name = 'usuario_form.html'
    form_class = RegistroForm
    success_url = reverse_lazy('home:homeapp')


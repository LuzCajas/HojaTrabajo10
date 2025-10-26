from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

# class EstudiantesView(TemplateView):
#     template_name = 'estudiantes.html'

# class AdminView(TemplateView):
#     template_name = 'admin.html'

# class AcercaView(TemplateView):
#     template_name = 'acerca.html'

class LoginView(LoginView):
    template_name = 'login.html'

def login_view(request):
    next_url = request.GET.get('next') 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:  
                return redirect(next_url)
            return redirect('home:homeapp')  
        else:
            context = {'error': 'Usuario o contraseña incorrectos', 'next': next_url}
            return render(request, 'home:login', context)
    return render(request, 'home:login', {'next': next_url})

def logout_view(request):
    logout(request)
    return redirect('home:homeapp')
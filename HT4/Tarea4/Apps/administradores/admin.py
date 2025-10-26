from django.contrib import admin
from .models import Administrador, Estudiante, Publicacion, Usuario
# Register your models here.

admin.site.register(Administrador)
admin.site.register(Estudiante)
admin.site.register(Publicacion)
admin.site.register(Usuario)

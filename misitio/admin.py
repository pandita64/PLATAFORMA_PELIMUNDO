

# Register your models here.
from django.contrib import admin
from .models import Categoria, Pelicula,ConfiguracionSitio

admin.site.register(Categoria)
admin.site.register(Pelicula)
admin.site.register(ConfiguracionSitio)


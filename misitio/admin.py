

# Register your models here.
from django.contrib import admin
from .models import Categoria, Pelicula,ConfiguracionSitio,ConfiguracionLogin,ConfiguracionRegistro

admin.site.register(Categoria)
admin.site.register(Pelicula)
admin.site.register(ConfiguracionSitio)
admin.site.register(ConfiguracionLogin)
admin.site.register(ConfiguracionRegistro)


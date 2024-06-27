from django.db import models



class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
class ConfiguracionSitio(models.Model):
    imagen_fondo = models.ImageField(upload_to='imagenes_fondo', null=True, blank=True)

    def __str__(self):
        return "Configuración del Sitio"
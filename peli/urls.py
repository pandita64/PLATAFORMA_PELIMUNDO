"""
URL configuration for peli project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from misitio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('pricipal/', views.pricipal, name='pricipal'),
    path('terror/', views.terror, name='terror'),
    path('series/', views.series, name='series'),
    path('infantiles/', views.infantiles, name='infantiles'),
    path('buscar_pelicula/', views.buscar_pelicula, name='buscar_pelicula'),
    path('cerrar/', views.cerrar, name='cerrar'),
    path('password_reset/', include('django.contrib.auth.urls')),
    path('misitio/', include('misitio.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# Agrega estas vistas a tu urls.py





# Configuración para servir archivos estáticos durante el desarrollo



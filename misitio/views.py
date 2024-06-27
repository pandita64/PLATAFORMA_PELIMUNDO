from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Pelicula, Categoria, ConfiguracionSitio, ConfiguracionLogin

def get_imagen_fondo():
    config = ConfiguracionSitio.objects.first()
    return config.imagen_fondo.url if config and config.imagen_fondo else None

@login_required
def home(request):
    peliculas = Pelicula.objects.all()
    imagen_fondo = get_imagen_fondo()
    return render(request, 'pricipal.html', {'peliculas': peliculas, 'imagen_fondo': imagen_fondo})

def signup(request):
    if request.user.is_authenticated:
        return redirect('pricipal')
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('pricipal')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error': 'User already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm(),
            'error': 'Passwords do not match'
        })
    
def login_view(request):
    if request.method == 'GET':
        try:
            # Obtén la configuración de fondo del login si existe
            configuracion_login = ConfiguracionLogin.objects.first()
            imagen_fondo = configuracion_login.imagen_fondo_login.url if configuracion_login and configuracion_login.imagen_fondo_login else None
        except ConfiguracionLogin.DoesNotExist:
            imagen_fondo = None

        return render(request, 'login.html', {
            'form': AuthenticationForm(),
            'imagen_fondo': imagen_fondo  # Pasa la URL de la imagen de fondo al contexto
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm(),
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('pricipal')

@login_required
def peliculas_categoria(request, categoria_nombre):
    categoria = Categoria.objects.get(nombre=categoria_nombre)
    peliculas = Pelicula.objects.filter(categoria=categoria)
    imagen_fondo = get_imagen_fondo()
    return render(request, 'pricipal.html', {'peliculas': peliculas, 'categoria': categoria, 'imagen_fondo': imagen_fondo})
    

def pricipal(request):
    peliculas = Pelicula.objects.all()
    imagen_fondo = get_imagen_fondo()
    return render(request, 'pricipal.html', {'peliculas': peliculas,'imagen_fondo': imagen_fondo})

@login_required
def terror(request):
    categoria_terror = Categoria.objects.get(nombre='Terror')
    peliculas = Pelicula.objects.filter(categoria=categoria_terror)
    imagen_fondo = get_imagen_fondo()
    return render(request, 'pricipal.html', {'peliculas': peliculas, 'categoria': categoria_terror, 'imagen_fondo': imagen_fondo})

@login_required
def series(request):
    categoria_series = Categoria.objects.get(nombre='Series')
    peliculas = Pelicula.objects.filter(categoria=categoria_series)
    imagen_fondo = get_imagen_fondo()
    return render(request, 'pricipal.html', {'peliculas': peliculas, 'categoria': categoria_series, 'imagen_fondo': imagen_fondo})

@login_required
def infantiles(request):
    categoria_infantiles = Categoria.objects.get(nombre='Infantiles')
    peliculas = Pelicula.objects.filter(categoria=categoria_infantiles)
    imagen_fondo = get_imagen_fondo()
    return render(request, 'pricipal.html', {'peliculas': peliculas, 'categoria': categoria_infantiles, 'imagen_fondo': imagen_fondo})

@login_required
def buscar_pelicula(request):
    if request.method == 'POST':
        nombre = request.POST.get('q')
        if Pelicula.objects.filter(titulo=nombre).exists():
            peliculas = Pelicula.objects.filter(titulo=nombre)
            imagen_fondo = get_imagen_fondo()
            return render(request, 'pricipal.html', {'peliculas': peliculas, 'imagen_fondo': imagen_fondo})
        else:
            return render(request, 'pricipal.html', {'msj': 'No se encontró', 'imagen_fondo': get_imagen_fondo()})
    else:
        return render(request, 'pricipal.html', {'msj': 'No se encontró', 'imagen_fondo': get_imagen_fondo()})

@login_required
def cerrar(request):
    logout(request)
    return redirect('login')








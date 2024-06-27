# misitio/urls.py
# misitio/urls.py
from django.urls import path
from .views import peliculas_categoria, home

urlpatterns = [
    path('', home, name='home'),
    path('peliculas/<str:categoria_nombre>/', peliculas_categoria, name='peliculas_categoria'),
]



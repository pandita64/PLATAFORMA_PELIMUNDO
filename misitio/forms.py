from django import forms
from.models import Pelicula

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ('nombre', 'imagen')
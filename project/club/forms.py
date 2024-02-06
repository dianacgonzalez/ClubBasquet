from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from . import models

class ProfeForm(forms.ModelForm):
    class Meta:
        model = models.Profe
        fields = "__all__"


class JugadorForm(forms.ModelForm):
    class Meta:
        model = models.Jugador
        fields = "__all__"


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = "__all__"


class EquipoForm(forms.ModelForm):
    class Meta:
        model = models.Equipo
        fields = "__all__"


class EquipoJugadorForm(forms.ModelForm):
    class Meta:
        model = models.EquipoJugador
        fields = "__all__"

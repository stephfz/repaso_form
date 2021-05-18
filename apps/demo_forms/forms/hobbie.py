from django import forms
from django.forms import widgets

from django.forms.models import fields_for_model

from ..models import Hobbie

class HobbieForm(forms.ModelForm):
    class Meta:
        OPCIONES_TIPO= [('0', '-- Seleccione --'),('1', 'Outdoors'), ('2', 'Indoors'), ('3', 'Ambos')]
        model = Hobbie
        fields = "__all__"
        widgets ={
            'tipo' : forms.Select(choices=OPCIONES_TIPO)
        }

